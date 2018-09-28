# Main Developer Tools

- Operating System (OS): For programming on desktops and laptops, we are mainly using the Desktop version of a GNU/Linux distribution called Ubuntu, which ISO can be downloaded [here](https://www.ubuntu.com/download/desktop). At time of writing, we are somewhere in the transition between `16.04` and `18.04`. Both are good options as they are Long-term support (LTS). For OS on robots, see [roboticslab-uc3m/questions-and-answers#20](https://github.com/roboticslab-uc3m/questions-and-answers/issues/20). Regarding installation on a desktop or laptop, there are several options:
   - Virtual Machine: Not very risky, as boot and partitions are not touched. However, possible issues with: enabling virtualization in BIOS, connecting devices such as USB webcam/RGB-D or Arduino, additional difficult configuration for networking beyond NAT (bridge adaptors, host firewalls, etc), and also possible adversities regarding access to graphic cards (e.g. NVIDIA drivers and CUDA). Still, good option for experimenting with new OS, and also to be able to work with different OS simultaneously.
   - Native Partition: More risky, as boot and partitions are touched. Please backup your data before doing this, and additionaly have an extra machine around in case you mess up your boot (may additional hours/days to fix, depending on expertize)! A basic recommendation towards avoiding data loss is to first manage partition sizes from within the original OS to leave empty space for the new OS. It is recommended to assume the risk if you want higher performance and/or are going to be interacting with hardware (e.g. cameras or real robots!). Basic steps:
      1. Download the ISO from the links above.
      1. Historically, ISOs were burnt to CDs, but now we create bootable USB drives. [This nice tutorial](https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows) via Windows recommends [Rufus](http://rufus.akeo.ie/).
      1. Create disk space for installation. If from Windows, best from Disk Administration tool.
      1. Turn off and reboot into USB (via boot selection or changing boot order in BIOS), install Ubuntu.
   - Windows Subsystem for Linux (WSL): [FAQ](https://docs.microsoft.com/en-us/windows/wsl/faq).
- Version control: [Tutorial (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/version-control/) / [Usage within roboticslab-uc3m organization](version-control.md)
- Github (issues, etc): [Tutorial](https://david-estevez.gitbooks.io/the-git-the-bad-and-the-ugly/content/)
- Markdown: [Tutorial (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/writing/markdown.html)
- CMake: [Tutorial (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/programming/cmake.html)
- C/C++: Low-level (control) programming. Some good slides on C are "Thinking in C" by Bruce Eckel, and some good books on C++ are "Thinking in C++" by Bruce Eckel.
- Python: High-level (algorithm) programming.
- Doxygen: Document code, within the code.
