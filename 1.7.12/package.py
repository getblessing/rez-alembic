
name = "alembic"

version = "1.7.12"

variants = [
    ["arch-*", "os-*", "release-1"],
    ["arch-*", "os-*", "release-0"],
]

build_requires = [
    "rezutil-1+",
    "cmake",
    "boost",
    "hdf5",
    "openexr",  # for ilmbase
]
build_command = "python {root}/rezbuild.py {install}"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/lib")
    env.LD_LIBRARY_PATH.prepend('{root}/lib/')
