# Commands list
|  command  |  short  |                                         info                                         |
|-----------|---------|--------------------------------------------------------------------------------------|
|  add      |         |  add offset from base 0x0 in arg0 with optional name for this target following args  |
|  attach   |  att    |  attach to target package name in arg0 with target module name in arg1               |
|  help     |  h      |                                                                                      |
|  memory   |  mem,m  |  memory operations                                                                   |
|  print    |  p,pr   |                                                                                      |
|  quit     |  q      |                                                                                      |
|  run      |  r      |  continue the execution of the process to the next target offset                     |
|  session  |  s,ss   |                                                                                      |

---
# memory sub commands
|  command  |  short  |                      info                       |
|-----------|---------|-------------------------------------------------|
|  read     |  rd,r   |  read memory from address in arg0 for len arg1  |

# session sub commands
|  command  |  short  |                                           info                                           |
|-----------|---------|------------------------------------------------------------------------------------------|
|  save     |  s,sv   |  saves current target offsets, package and module to be immediatly executed with 'load'  |
|  load     |  l,ld   |  load session from previously saved information                                          |

---
# memory read sub commands
|  command  |  short  |                 info                  |
|-----------|---------|---------------------------------------|
|  pointer  |  p,ptr  |  read a pointer from address in arg0  |
