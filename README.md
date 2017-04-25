# rename-coursera
Problem: when you download files from coursera, they often include nasty characters \ / : * ? " < > | in their filenames. You run into problems with certain cloud file hosting platforms such as OneDrive, which don't allow for such filenames. Your files don't sync to the cloud and you are stuck. Renaming them manually by removing those nasty characters would be a chore.

Idea: write a python script that automatically scans your directory for nasty filenames, and converts the nasty characters to OneDrive friendly dashes - instead, so that they may happily sync to the cloud again.
