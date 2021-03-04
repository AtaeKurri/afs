# AFS (Atae File System)

A small module (the main one being afs_memory.py) to reproduce how a .dat file would work.
I tried to make my own version of a .dat file.

# Usage

You can use any of the 3 files independently from one another.
But remember to change the commented line in every file with a string containing a fernet token.
To generate a fernet token, just use this :
```python
from cryptography.fernet import Fernet
print(Fernet.generate_key())
```
And put it in the line that says :
```python
key = Fernet(f"{open("key.txt", "r").read()}")
```

You can import afs_memory as a module using :
```python
from .afs_memory import afs_memory as afs
```

You now have access to the afs module.

You need to create an instance of the afs_memory class :
```python
c_f = afs.afs_memory("your_file.afs")
```

### j_load

A method used to load the your_file.afs file into the memory in json format.

Example from my [Stellarium discord bot](https://github.com/AtaeKurri/Stellarium) :
```python
conf = c_f.j_load
```

Returns the content in json format of your_file.afs

### write_json_to_afs()

This method is used to edit a json dict.

Example from my [Stellarium discord bot](https://github.com/AtaeKurri/Stellarium) :
```python
c_f = afs.afs_memory("db.afs")
conf = c_f.j_load

conf["serverconfig"][str(ctx.guild.id)]["cmds"][cmd] = cmd
c_f.write_json_to_afs(c_f.j_load, conf)
```

You need to specify the dict structure before it was changed and after it was changed.

### delete_json_from_afs()

This method is used to remove a key from a json dict.

Example from my [Stellarium discord bot](https://github.com/AtaeKurri/Stellarium) :
```python
c_f = afs.afs_memory("db.afs")
conf = c_f.j_load

c_f.delete_json_from_afs(conf, f"serverconfig.{str(ctx.guild.id)}.cmds.{cmd}")
```

You need to specify the dict structure before it was changed (first argument)
You need a path string for the deletion of the keys in the first argument.
Must be in this format :
    Given this dict path : `conf["serverconfig"]["an_id"]["cmds"]`
    the second argument must be this string : "serverconfig.an_id.cmds"
Will then delete the "cmds" key from the dict conf in the path `["serverconfig"]["an_id"]`