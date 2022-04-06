# Programming with YARP

## Programming in C++ with YARP

* We usually derive our base classes from [yarp::os::RFModule](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html), thus inheriting a [configure\(yarp::os::ResourceFinder& rf\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a6c3880961b00b0a7eb527d62214169b7) method that receives a map \([rf](http://www.yarp.it/classyarp_1_1os_1_1ResourceFinder.html)\) passed from `main()`, a [close\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a58ce26fc6fdcb6eb4af8e8dc678e095e) that gets called by _CRTL+C_, and a [updateModule\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a37ee5baa17ce243458a1dff209e878b7) which is invoked with a periodicity measured in seconds given by [getPeriod\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#ace2fdadde1a2690f274079fabd6420d2). In case you need a function that gets called more often, you may inherit the [run\(\)](http://www.yarp.it/classyarp_1_1os_1_1PeriodicThread.html#a4585b8555a7b796aff7b2ba8b0c8343d) method from [yarp::os::PeriodicThread](http://www.yarp.it/classyarp_1_1os_1_1PeriodicThread.html) and obtain a periodicity given in seconds wih double precision, to be specified in the constructor.
* Implement your device as a class, and ideally as a YARP device ([tutorial (Spanish)](https://apps-robots.uc3m.es/asrob/wiki/Tutorial_yarp_devices)).

### Regarding `close()`

If there exists a `close` method that needs to release unmanaged resources (dynamically allocated memory) or terminate stuff in an ordered manner (if using `PolyDriver` class members, e.g. `close` device A before device B), always define a class destructor that calls `close`, be it a `DeviceDriver` or an `RFModule` derived class. Also, make sure nothing bad happens if this `close` method is called several times (i.e. set dangling pointers to `nullptr`). Why is that:
- `PolyDriver::open` may fail to initialize a subdevice, but it does not call the subdevice's `close` method; instead, it is immediately destructed via delete ([ref](https://github.com/robotology/yarp/blob/b3dff81c3739112b8f65cfd808f129bcbf4e7aa5/src/libYARP_dev/src/yarp/dev/PolyDriver.cpp#L308)).
- If `RFModule::configure` returns false, as explained in the above comments, `close` will never be called, hence we also want to use a destructor here.
- `PolyDriver::close` will never close a wrapped device twice, but callers of `RFModule` can do that inadvertently because of the previous point: once after a successful `RFModule::configure` and a `CTRL+C` signal (it just stops execution flow and calls close before leaving `runModule`), and one more time on class destruction.
- Despite those two mechanisms being relatively different, this policy ensures we treat both `RFModule` and `DeviceDriver` constructs in a similar manner: `close()` on destruction, avoid dangling pointers.

## Similar and Related

* [Appendix: YARP Tricks](appendix/yarp-tricks.md)
* [Install YARP](https://robots.uc3m.es/installation-guides/install-yarp.html) ([perma](https://github.com/roboticslab-uc3m/installation-guides/blob/00b8999eeb124e2c05aa37a46b9f23450b1343fe/install-yarp.md))
    * [Install YARP: Similar and Related](https://robots.uc3m.es/installation-guides/install-yarp.html#similar-and-related) ([perma](https://github.com/roboticslab-uc3m/installation-guides/blob/00b8999eeb124e2c05aa37a46b9f23450b1343fe/install-yarp.md#similar-and-related))

## If you have any doubts or comments

Please read the [Asking Questions](asking-questions.md) section, and once you've succeded with its [self-evaluation](asking-questions.md#self-evaluation-time) follow the recommendations by commenting publicly [HERE](https://github.com/roboticslab-uc3m/developer-manual/issues/new) if required
