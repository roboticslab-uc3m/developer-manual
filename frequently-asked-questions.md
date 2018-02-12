# Frequently Asked Questions

## How can I record data for Programming by Demonstration (PbD) a.k.a. Learning from Demonstration (LfD)?

First, if moving the robot by hand, you'll want some gravity compensation to help out. That's `[gcmp]` off `BasicCartesianControl`. Refer to the [BasicCartesianControl documentation](http://robots.uc3m.es/dox-kinematics-dynamics/group__BasicCartesianControl.html) for reference.

Once you have publishing services running (robot joint/cartesian state, sensors output), there are two options for recording data:

1. Manually grab "waypoints" or sensor data and store in file(s). For instance, in the joint space, do some `yarp rpc /robotName/manipulatorName/rpc:i` to get joint positions.

1. Use [yarpdatadumper](http://www.yarp.it/yarpdatadumper.html) ([related](http://www.yarp.it/yarpdatadumperAppGenerator.html)) to record the full trajectory.

## How can I play back data recorded for Programming by Demonstration (PbD) a.k.a. Learning from Demonstration (LfD)?

Depending on options above:

1. You can use the waypoints in a program as in [this example](https://github.com/roboticslab-uc3m/yarp-devices/tree/73cbd201df69ee19662cdb26a83d898669834bcb/example/cpp/exampleRemoteControlboard).

1. Use stuff from our [tools](https://github.com/roboticslab-uc3m/tools) repository. Specifically, you'll want the [PlaybackThread](https://github.com/roboticslab-uc3m/tools/tree/a7be63dc53090a5ca4ed19dc078ab3823aac1be3/libraries/ToolsYarpPlugins/PlaybackThread). You can find an example of use at [examplePlaybackThread](https://github.com/roboticslab-uc3m/tools/tree/a7be63dc53090a5ca4ed19dc078ab3823aac1be3/example/cpp/examplePlaybackThread) and its corresponding [test](https://github.com/roboticslab-uc3m/tools/blob/a7be63dc53090a5ca4ed19dc078ab3823aac1be3/tests/testPlaybackThread/testPlaybackThread.cpp).

Note: There are several alternatives to these approaches, but these are kind of nice. [yarpmanager](http://www.yarp.it/yarpmanager.html) has some record/playback facilities, but we haven't really tried them. Additionally, [yarpdataplayer](http://www.yarp.it/yarpdataplayer.html) does some playback, but for me it's nice to have something like what we have in the previously mentioned [tools](https://github.com/roboticslab-uc3m/tools) repository because it is a small library that can be used independently and is not coupled with any graphical interface.
