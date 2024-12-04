from miniz.miniz import Miniz

try:
    print(Miniz.decompress(bytes.fromhex('78010dc2390a80400c05d052b4d4ce4a3c8024933fdb719259c046c1c2f32bbc696ba098cd92b23242ed66625db568498d106d5e22e0202e4b622f082c24eba0577deeb3eee34bfe20fa7df036131b0000f53a00000000')))
except:
    pass