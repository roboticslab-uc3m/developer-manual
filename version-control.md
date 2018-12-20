# Version control

* **For any kind of project, as insignificant as it may seem**, use one of our shared repositories:
  * Software and hardware: [GitHub \(public GIT\)](https://github.com/roboticslab-uc3m). We follow the [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow/) git workflow \(except pure documentation repos, see [\#6](https://github.com/roboticslab-uc3m/developer-manual/issues/6)\) with [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) and [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration). Take advice from your advisor/supervisor \(who may direct you to [Juan](https://github.com/jgvictores), [David](https://github.com/David-Estevez) or [Raúl](https://github.com/rsantos88)\) if it's not clear to which repository you should refer. Adjust [.gitignore](https://git-scm.com/docs/gitignore) for the right project type to prevent from uploading unwanted files \(binaries, backups and leftover code\).
  * Paper writing: consult your advisor/supervisor \(who may direct you to [Juan](https://github.com/jgvictores)\) for the exact URL at [http://robots.uc3m.es/svn/\*](http://robots.uc3m.es/svn/*) \(private SVN\).

## Guidelines for contributing to projects using Version control

* Upload your work to a new branch, branching out from `develop`. If `develop` doesn't exist, branch out from `master` instead.
* Whenever you feel your changes are mature enough to be merged with the main project, create a Pull Request. Your work will be reviewed and merged by the owner/admin of that repository.
* Use a short and direct commit message that clearly states the changes made in that commit. Avoid using generic messages such as "Upload files", since they make it very hard for the repository users to track changes later on.
* Avoid uploading zip and binary files. In most cases, uploading the sources will suffice to generate the rest of the files.
* Upload your changes / files in the corresponding folder, and use a concise and explanatory name for your files. Try to be coherent with the rest of the files in that repositories (CamelCase, kebab-case, etc).
* In case of doubt, please ask.


