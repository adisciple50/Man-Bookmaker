__author__ = 'Jason Crockett'

import dbm.gnu as gdbm
import subprocess
import os as terminal
import gz

def getArticles(verbose):
    with gdbm.open("/var/cache/man/index.db", "r") as IndexDb:
        IndexDb = IndexDb.keys()
        if verbose:
            print("contents:", IndexDb)
        Articles = []
        for Article in IndexDb:
            Articles.append(bytes(Article).decode()[:-1])
        if verbose:
            print(Articles)
        return Articles

def generateArticles(verbose,ProgramList,ManParamsList=[],FileExtension=".txt"):
    assert(isinstance(ManParamsList,list))
    try:
        terminal.mkdir("~/.CatManFiles")
    except OSError:
        print([OSError, " ...continuing anyway"])
        pass

    for Program in ProgramList:
        Filename = "~/.CatManFiles/" + str(Program) + str(FileExtension)
        Command = ["man"] + ManParamsList + [Program] #, "|", "cat"] - possibly overkill
        Article = subprocess.check_output(Command)
        # see above : gets stdout (console output of a cli program).
        # ... that runs as a seperate program
        if verbose:
            print(["Running:",Command])
            print(Article)
            print(["Saving To File:", Filename])
        try:
            with terminal.open(Filename,[]) as CatManFile:
                CatManFile.write(Article)
        except FileExistsError:
            if verbose:
                print([FileExistsError, ". Skipping to next man article"])
            continue
    return True

def runLocalTest():
    Articles = getArticles("yes")
    generateArticles("yes",Articles)

runLocalTest()

def getFileList(FolderPath):
	FileList = [ f for f in listdir(FolderPath) if isfile(join(FolderPath,f)) ]
	return FileList
