<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://vjs.zencdn.net/6.6.3/video-js.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/aws-sdk/2.278.1/aws-sdk.min.js"></script>
        <title>Wegis Kinesis Video Streams HLS Viewer</title>
        <style>
            .disnon{display:none!important;}
        </style>
    </head>
    <body>
        <!--a href="https://github.com/aws-samples/amazon-kinesis-video-streams-hls-viewer"><img style="position: absolute; top: 0; left: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_left_orange_ff7600.png" alt="Fork me on GitHub"></a-->
        <?php
            
            //$accessKeyId = $_GET['id'];
            //$secretAccessKey = $_GET['pw'];
        ?>
        
        <div>
            <!--h1 style="margin: 20px 0;">위지스 스트리밍 서비스 유후~!</h1-->
            <div>
                <div class="col-md-4 start_btn">
                    <div class="form-group disnon">
                        <label>Player</label>
                        <select id="player" class="form-control form-control-sm">
                            <option selected>VideoJS</option>
                            <option>Shaka Player</option>
                        </select>
                    </div>
                    <div class="form-group disnon">
                        <label>Region</label>
                        <select id="region" class="form-control form-control-sm">
                            <option>ap-northeast-1</option>
                            <option>eu-central-1</option>
                            <option>eu-west-1</option>
                            <option>us-east-1</option>
                            <option selected>us-west-2</option>
                        </select>
                    </div>
                    <div class="form-group disnon">
                        <label>엑세스키</label>
                        <input id="accessKeyId" value="<?php echo $accessKeyId?>" type="password" class="form-control form-control-sm"/>
                    </div>
                    <div class="form-group disnon">
                        <label>비밀키</label>
                        <input id="secretAccessKey" value="<?php echo $$secretAccessKey?>" type="password" class="form-control form-control-sm"/>
                    </div>
                    <div class="form-group disnon">
                        <label>AWS Session Token (Optional)</label>
                        <input id="sessionToken" type="password" class="form-control form-control-sm" />
                    </div>
                    <div class="form-group disnon">
                        <label>Endpoint (Optional)</label>
                        <input id="endpoint" type="text" class="form-control form-control-sm" />
                    </div>
                    <div class="form-group disnon">
                        <label>Stream name</label>
                        <input id="streamName" value="MeerkatVideoStream" type="text" class="form-control form-control-sm"/>
                    </div>
                    <div class="form-group disnon">
                        <label>Playback Mode</label>
                        <select id="playbackMode" class="form-control form-control-sm">
                            <option selected>LIVE</option>
                            <option>ON_DEMAND</option>
                        </select>
                    </div>
                    <div class="form-group disnon">
                        <label>Start Timestamp</label>
                        <input id="startTimestamp" type="datetime-local" class="form-control form-control-sm"/>
                    </div>
                    <div class="form-group disnon">
                        <label>End Timestamp</label>
                        <input id="endTimestamp" type="datetime-local" class="form-control form-control-sm"/>
                    </div>
                    <div class="form-group disnon">
                        <label>Fragment Selector Type</label>
                        <select id="fragmentSelectorType" class="form-control form-control-sm">
                            <option selected>SERVER_TIMESTAMP</option>
                            <option>PRODUCER_TIMESTAMP</option>
                        </select>
                    </div>
                    <div class="form-group disnon">
                        <label>Discontinuity Mode</label>
                        <select id="discontinuityMode" class="form-control form-control-sm">
                            <option selected>ALWAYS</option>
                            <option>NEVER</option>
                        </select>
                    </div>
                    <div class="form-group disnon">
                        <label>Max Media Playlist Fragment Results</label>
                        <input id="maxMediaPlaylistFragmentResults" type="text" class="form-control form-control-sm"/>
                    </div>
                    <div class="form-group disnon">
                        <label>Expires (seconds)</label>
                        <input id="expires" type="text" class="form-control form-control-sm"/>
                    </div>
                    <button id="start" type="submit" class="btn btn-primary">Start Playback</button>
                </div>
                <br />
                <br />
                <div>
                    <div id="playerContainer">

                        <!-- VideoJS elements -->
                        <video id="videojs" class="player video-js vjs-default-skin" controls autoplay></video>
                        <script src="https://vjs.zencdn.net/6.6.3/video.js"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/videojs-contrib-hls/5.14.1/videojs-contrib-hls.js"></script>=
                        <!-- Shaka Player elements -->
                        <!--video id="shaka" class="player" controls autoplay></video>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/shaka-player/2.4.1/shaka-player.compiled.js"></script-->
                    </div>

                    <!--h3 style="margin-top: 20px;">Logs</h3-->
                    <div class="card bg-light mb-3 disnon">
                        <pre id="logs" class="card-body text-monospace" style="font-family: monospace; white-space: pre-wrap;"></pre>
                    </div>
                </div>
            </div>
        </div>
        <script>
            configureLogging();

            $('#start').click(function() {
                var streamName = $('#streamName').val();

                // Step 1: Configure SDK Clients
                var options = {
                    accessKeyId: $('#accessKeyId').val(),
                    secretAccessKey: $('#secretAccessKey').val(),
                    sessionToken: $('#sessionToken').val() || undefined,
                    region: $('#region').val(),
                    endpoint: $('#endpoint').val() || undefined
                }
                var kinesisVideo = new AWS.KinesisVideo(options);
                var kinesisVideoArchivedContent = new AWS.KinesisVideoArchivedMedia(options);

                // Step 2: Get a data endpoint for the stream
                console.log('Fetching data endpoint');
                kinesisVideo.getDataEndpoint({
                    StreamName: streamName,
                    APIName: "GET_HLS_STREAMING_SESSION_URL"
                }, function(err, response) {
                    if (err) { return console.error("key error "+err); }
                    console.log('Data endpoint: ' + response.DataEndpoint);
                    kinesisVideoArchivedContent.endpoint = new AWS.Endpoint(response.DataEndpoint);

                    // Step 3: Get an HLS Streaming Session URL
                    console.log('Fetching HLS Streaming Session URL');
                    kinesisVideoArchivedContent.getHLSStreamingSessionURL({
                        StreamName: streamName,
                        PlaybackMode: $('#playbackMode').val(),
                        HLSFragmentSelector: {
                            FragmentSelectorType: $('#fragmentSelectorType').val(),
                            TimestampRange: $('#playbackMode').val() === "LIVE" ? undefined : {
                                StartTimestamp: new Date($('#startTimestamp').val()),
                                EndTimestamp: new Date($('#endTimestamp').val())
                            }
                        },
                        DiscontinuityMode: $('#discontinuityMode').val(),
                        MaxMediaPlaylistFragmentResults: parseInt($('#maxMediaPlaylistFragmentResults').val()),
                        Expires: parseInt($('#expires').val())
                    }, function(err, response) {
                        if (err) { return console.error(err); }
			/*json변수값비교
                        console.log('HLS Streaming Session URL: ' + response.HLSStreamingSessionURL);

                        // Step 4: Give the URL to the video player.
                        var playerName = $('#player').val();
                        if (playerName === 'VideoJS') {
                            var playerElement = $('#videojs');
                            playerElement.show();
                            var player = videojs('videojs');
                            console.log('Created VideoJS Player');

                            player.src({
                                src: response.HLSStreamingSessionURL,
                                type: 'application/x-mpegURL'
                            });
                            console.log('Set player source');

                            player.play();
                            console.log('Starting playback');
                        } else if (playerName === 'Shaka Player') {
                            var playerElement = $('#shaka');
                            playerElement.show();

                            var player = new shaka.Player(playerElement[0]);
                            console.log('Created Shaka Player');

                            player.load(response.HLSStreamingSessionURL).then(function() {
                                console.log('Starting playback');
                            });
                            console.log('Set player source');
                        }
                    });
                });
                $('.start_btn').hide();
                $('.player').hide();
            });

            // Read/Write all of the fields to/from localStorage so that fields are not lost on refresh.
            [
                'player',
                'region',
                'accessKeyId',
                'secretAccessKey',
                'sessionToken',
                'endpoint',
                'streamName',
                'playbackMode',
                'startTimestamp',
                'endTimestamp',
                'fragmentSelectorType',
                'discontinuityMode',
                'maxMediaPlaylistFragmentResults',
                'expires'
            ].forEach(function(field) {
                var id = "#" + field;

                // Read field from localStorage
                try {
                    var localStorageValue = localStorage.getItem(field);
                    if (localStorageValue) { $(id).val(localStorageValue); }
                } catch (e) { /* Don't use localStorage */ }

                // Write field to localstorage on change event
                $(id).change(function() {
                    try {
                        localStorage.setItem(field, $(id).val());
                    } catch (e) { /* Don't use localStorage */ }
                });
            });

            // Setup disabled/enabled state for timestamp fields
            $('#playbackMode').change(function() {
                updateTimestampFieldState();
            });
            updateTimestampFieldState();

            // Initially hide the player elements
            $('.player').hide();

            function configureLogging() {
                console._error = console.error;
                console.error = function(messages) {
                    log('ERROR', Array.prototype.slice.call(arguments));
                    console._error.apply(this, arguments);
                }

                console._log = console.log;
                console.log = function(messages) {
                    log('INFO', Array.prototype.slice.call(arguments));
                    console._log.apply(this, arguments);
                }

                function log(level, messages) {
                    var text = '';
                    for (message of messages) {
                        if (typeof message === 'object') { message = JSON.stringify(message, null, 2); }
                        text += ' ' + message;
                    }
                    $('#logs').append($('<div>').text('[' + level + ']' + text + '\n'));
                }
            }

            function updateTimestampFieldState() {
                var isLive = $('#playbackMode').val() === 'LIVE';
                $('#startTimestamp').prop('disabled', isLive);
                $('#endTimestamp').prop('disabled', isLive);
            }

            console.log("Page loaded")
        </script>
        <style>
            #playerContainer, .player { width: 100%; height: auto; min-height: 700px; background-color: black; }
            .vjs-big-play-button { display: none !important; }
        </style>
    </body>
</html>

