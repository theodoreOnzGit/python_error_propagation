import metrolopy as uc

## create gummy quantity
# Gummy is named because of GUM
# on the metrolopy website:
# "The name comes from the JGCM/ISO Guide to the
# Expression of Uncertainty in Measurement which is also known as the GUM."
# you can see it in the references in the readme

# we are going to try to have some examples of

h1 = uc.gummy(1.050, u=0.001, unit="m")
h2 = uc.gummy(1.061, u=0.001, unit="m")

delta_h = h2 - h1

print("\n heights, h1, h2 and delta_h \n")
print(h1)
print(h2)
print(delta_h)
