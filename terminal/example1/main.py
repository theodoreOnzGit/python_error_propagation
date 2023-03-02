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

# we next want to do g, appropriate units can be found
# This method only works for jupyter though
print("\n setup gravity, print all units! \n")
uc.search_units("acceleration", fmt="html")
# this works here

uc.search_units("acceleration", fmt="utf-8", show_all=True)

# the units for acceleration are galileo
# or cm/s^2
# we shall convert it to SI,
# 1 hectogalileo, hGal = 1 ms^{-2}

g = uc.gummy(9.80, u=0.03, unit="hGal")

print("\n gravity in SI units")
print(g)

# if you want standard formatting with plus and minus:
g.style = "+-"
print(g)


# now for density
# you will find that density (as of feb 2023) doesn't work,
# in fact, density units are missing from here
print("\n Try to get density units, we don't get the right answer...\n")
uc.search_units("density", fmt="utf-8", show_all=False)
# this doesn't quite work for density, because we'll get
# magnetic flux density

# so we'll have a workaround, volume and mass exist,
# so we can do those
print("\n Try to get volume units and mass units ")
uc.search_units("volume", fmt="utf-8", show_all=True)

# we take 1 kiloLiter which is 1 m3
# with zero uncertainty
one_meter_cubed = uc.gummy(1, u=0.0, unit="kL")

# we then add the mass which is 1061 kg with +- 0.05
# uncertainty
fluid_mass = uc.gummy(1061, u=0.05, unit="kg")

density = fluid_mass / one_meter_cubed
print("\n here's our clunky way for obtaining density \n")
print(density)

# now lets find our pressure drop

pressure = delta_h * density * g

print("\n now let's get our pressure drop: \n")
print(pressure)
# the units need to be corrected, doesn't work all the time though!
# of course, format this nicely...
pressure.unit = "Pa"
pressure.style = "+-"
print(pressure)

print("\n =================   end of tutorial ============== \n")
