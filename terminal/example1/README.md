# Basics of metrolopy

Uncertainty measurement can be tedious and harddd. Thankfully
we have a python package that can help us measure uncertainty
in python code called metrolopy.

The metrolopy has its own tutorial, so the material I provide is
supplementary to that. 
The examples are specific to fluid mechanics and heat transfer.

## Hydrostatic Pressure Example

$$ \Delta P = \Delta h \rho g$$

We can find the pressure drop across a series of pipes or a loop
using manometers. Presuming we know the height difference
of the manometer $\Delta h$, the fluid density $\rho$ and
the gravitational acceleration, g. We can then find the 
pressure drop P.

Now, if each manometer reading has an error of $\pm 1mm$, 
what is the error effect on $\Delta h$?

According to the GUM guidelines (Guide to the expression
of uncertainty in measurement) by the Joint Committee for
Guides in Metrology (JCGM, also btw, i think Metrolopy
gets its name from here), we can use the following formula:

$$u_c^2(\Delta h) = u^2(h_2) (\frac{\partial \Delta h}{h_2})^2
u^2(h_1) (\frac{\partial \Delta h}{h_1})^2)$$



