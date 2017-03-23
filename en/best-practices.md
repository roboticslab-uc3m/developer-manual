# Best practices

- **For any kind of project, as insignificant as it may seem**, use one of our shared repositories:
  - Software and hardware: [GitHub (public GIT)](https://github.com/roboticslab-uc3m). Take advice from your tutor/supervisor (who may direct you to [Juan](https://github.com/jgvictores), [David](https://github.com/David-Estevez) or [Raúl](https://github.com/rsantos88)) if it's not clear which repository you should refer to. Adjust [.gitignore](https://git-scm.com/docs/gitignore) for the right project type to prevent from uploading unwanted files (binaries, backups and leftover code).
  - Paper writing: consult your tutor (who may direct you to [Juan](https://github.com/jgvictores)) for the exact URL at http://robots.uc3m.es/svn/* (private SVN).
- **If you have a question, do a search first on our [wiki](http://robots.uc3m.es/) and among open and closed issues of the repository associated to your project**. In case you don't find the right answer, **open an issue in said repository or add a comment in the *Discussion* tab on the wiki**. Pros:
  - Increased global productivity as logs are kept. It tends to avoid repetition of the same questions and the same answers.
  - A convenient tool to keep any technical topic inside its technical context and focus on the proper issue's subject.
  - Higher visibility of your topic in such a way that the answer may come from unexpected people. This is especially interesting in cases of disagreement between two parties where unrelated contributors may bring up new ideas and worthy viewpoints.
- In case of trouble during installation of dependencies or additional software, take a look first at our [dedicated repository](https://www.gitbook.com/book/roboticslab-uc3m/installation-guides/details).
- The preferred way of documenting things (except Doxygen for C/C++) is Markdown.

## General programming
- Indent your code as if everything were Python. [astyle](http://astyle.sourceforge.net/) can handle this quite automatically for you (use with caution).
- DON'T ADD DIGITS to filenames as a hint of a specific version, iteration step, etc. - that is what hashes and tags in source control are for.
- AVOID DUPLICATES of existing programs. Prior to creating a new program, thoroughly analyze whether you can enhance an existing one through adjustment or implementation of new parameters. Once you are sure that the functionality of a program could be extended, proceed with the usual steps (open an issue or fork & create a pull request).
- Any `toDo`, `fixMe`, etc. inlined in code must be associated to an *open issue* (with bidirectional reference).
- [Headers, config files and CLI parameters](http://robots.uc3m.es/dox-asibot-main/post_install.html#post_install_changing_parameters).
- Read about [Clean code](https://www.google.es/search?q=cleancode).

## Programming in C/C++
- Use [project-generator](https://github.com/roboticslab-uc3m/project-generator) for creation of new C/C++ projects.
- Report any problems with project-generator in its corresponding [issues section](https://github.com/roboticslab-uc3m/project-generator/issues). If you find that this solution doesn't suit you, at least stick to [CMake](http://asrob.uc3m.es/index.php/Tutorial_CMake) for any C/C++ project.
- Use *UpperCamelCase* for library and class names.
- Use *lowerCamelCase* for executable names.
- Avoid global variables.
- We prefer modern `std::string` class to alternatives like `char*` or `yarp::os::ConstString`.
- Store your classes inside a *namespace* block.
- Keep a minimalistic `main()` by implementing your program as an OO class.
  - In C++, we usually derive our base classes from [yarp::os::RFModule](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html), thus inheriting a [configure(yarp::os::ResourceFinder& rf)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a6c3880961b00b0a7eb527d62214169b7) method that receives a map ([rf](http://www.yarp.it/classyarp_1_1os_1_1ResourceFinder.html)) passed from `main()`, a [close()](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a58ce26fc6fdcb6eb4af8e8dc678e095e) that gets called by *CRTL+C*, and a [updateModule()](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a37ee5baa17ce243458a1dff209e878b7) which is invoked with a periodicity measured in seconds given by [getPeriod()](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#ace2fdadde1a2690f274079fabd6420d2). In case you need a function that gets called more often, you may inherit the [run()](http://www.yarp.it/classyarp_1_1os_1_1RateThread.html#ac3c97e766733b41a45c799aa0c05598f) method from [yarp::os::RateThread](http://www.yarp.it/classyarp_1_1os_1_1RateThread.html) and obtain a periodicity given in milliseconds, to be specified in the constructor.
- Implement your device as a class, and ideally as a [*YARP device*](http://asrob.uc3m.es/index.php/Tutorial_yarp_devices).
- Create and maintain unit tests for each class. We are currently using **gtest**, see [kinematics-dynamics/test/testKdlSolver](https://github.com/roboticslab-uc3m/kinematics-dynamics/tree/develop/test/testKdlSolver.cpp) and [yarp-devices/tests/testTechnosoftIpos](https://github.com/roboticslab-uc3m/yarp-devices/tree/develop/tests/testTechnosoftIpos/testTechnosoftIpos.cpp).
