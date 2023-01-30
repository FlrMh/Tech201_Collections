Story1 = {
    "start": "Once upon a time, there was a young snail girl, named Petunia. Petunia was living in a magical forest, with insects and animals with superpowers. But, Petunia never felt like she belonged in this forest, as she could never find her super power.",
    "middle": "One day, the forest was attacked by a flock of radioactive crows, and they were a huge danger to the little insects in the forest. The animals with superpowers tried their best to fight the crows, but in vein. Nobody could protect the insects. Petunia was feely more worthless than ever. Until one moment! During one of the radioactive crows` raid over the forest, a family of ants was exposed and they were in great danger. Petunia was next to them and decided to cover the ants with her body, hoping the shell will protect them. But the crows hit Petunia`s shell and throw her on the side. Worried, Petunia comes out of her shell. Unbelievable! Petunia`s slime was magical, and created a protective wall between the ants and the crows! Desperate, the crows leave.",
    "end": "Everyone from the forest witnessed the attack and that is when everyone realised, including Petunia, that she is also magical! From that moment on, Petunia knew that she needed to dedicate her existance within the forest to protecting the smaller and helpless creatures around her. That was the day when she became THE SLIME GIRL!"
}

print(Story1)

print(type(Story1))

print(Story1.keys())

print(Story1.values())

print(Story1.get("start"))
print(Story1.get("middle"))
print(Story1.get("end"))

#or

print(Story1["start"])
print(Story1["middle"])
print(Story1["end"])

new_key = "hero"
new_value = "The Slime Girl"

Story1["hero"] = "The Slime Girl"
print(Story1)