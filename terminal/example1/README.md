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

$$u_c^2(\Delta h) =\left( u^2(h_2) (\frac{\partial \Delta h}{h_2})^2+
u^2(h_1) (\frac{\partial \Delta h}{h_1})^2 \right)$$

Where 

$$\Delta h = h_2 - h_1$$

For addition and subtraction cases like these in general:

$$u_c^2(\Delta h) = u^2(h_2) (1)^2+
u^2(h_1) (-1)^2 $$

The square cancels the $-1$ out and we don't really need to worry about
the signs. 

Great, now what about $\rho$ and $g$? What are their associated
uncertainties and how do they stack? 
We can use the same expression which is derived from a Taylor
Series expansion.


$$u_c^2(\Delta P) = u^2(g)  (\frac{\partial \Delta P}{g})^2+
u^2(\rho) (\frac{\partial \Delta P}{\rho})^2+
u^2(\Delta h) (\frac{\partial \Delta P}{\Delta h})^2 $$

$$u_c^2(\Delta P) = u^2(g)  (\frac{ \Delta P}{g})^2+
u^2(\rho) (\frac{ \Delta P}{\rho})^2+
u^2(\Delta h) (\frac{ \Delta P}{\Delta h})^2 $$

In general, for multiplication and division, we'll need to sum up
the fractional uncertainty using a sum of squares method.

Earth has a gravity of 9.81 $m s^{-2}$. And you can make the 
measurement uncertainty almost negligible if you have
the right equipment. Eg. Dropping atoms. So that
$\Delta g/g \approx 3e-9$

```
Peters, A., Chung, K. Y., & Chu, S. (1999). Measurement of gravitational 
acceleration by dropping atoms. Nature, 400(6747), 849-852.
```

Of course, gravity can also can vary from place to place on earth
due to altitude and rotation
For example,
the Nevado Huascarán summit (Peru) has a measured acceleration 
of $9.76392 m s^{−2}$ and the arctic sea has a measured
gravitational acceleration of $9.83366 m s^{−2}$. A root
mean square value of this is about $9.80133m s^{−2}$.

```
Hirt, C., Claessens, S., Fecher, T., Kuhn, M., Pail, R., & Rexer, M. (2013). 
New ultrahigh‐resolution picture of Earth's gravity field. Geophysical 
research letters, 40(16), 4279-4283.
```

So we can essentially account for this variation using

$$g = 9.80 \pm 0.03 m s^{-2}$$

We commonly like to use $9.81  m s^{-2}$ which is most definitely
within this range. We can of course factor this in our uncertainty
calculation as well if we expect the hydrostatic pressure measurement
formula to work all over the earth. We can be more precise if
we want to just have it in one place.

The density of the fluid depends on what we are using. For Therminol VP-1
or eutectic mixture of biphenyl and diphenyl ether
at 20 C we can use is $5e-4 gcm^{-3}$. 
```
Cabaleiro, D., Pastoriza-Gallego, M. J., Piñeiro, M. M., 
Legido, J. L., & Lugo, L. (2012). Thermophysical properties of 
(diphenyl ether+ biphenyl) mixtures for their use as heat transfer fluids. 
The Journal of Chemical Thermodynamics, 50, 80-88.
```
Hence, we use an estimated density of 
$1061  \pm 0.5 kg m^{-3}$, for Therminol VP-1
at 20 C.  Though you can see here, we need to do unit conversion. Which
is tedious.

Suppose we use 

$$\Delta h = h_2 - h_1 $$
$$h_1 = 1.050 \pm 0.001 m$$
$$h_1 = 1.061 \pm 0.001 m$$
$$g = 9.80 \pm 0.03 m s^{-2}$$
$$\rho = 1061  \pm 0.5 kg m^{-3}$$

What is our uncertainty?

First let's calculate our pressure, we are not
rounding off yet until we find our uncertainty:
$$\Delta P = 114.3758~Pa~\text{(pending round off)}$$

Also, for most values here, we won't round off till the last part.

$$\delta \Delta h = u(\Delta h) = \sqrt{0.001^2+0.001^2} m = 0.00141 m$$


We substitute into this expression:
$$u_c^2(\Delta P) = u^2(g)  (\frac{ \Delta P}{g})^2+
u^2(\rho) (\frac{ \Delta P}{\rho})^2+
u^2(\Delta h) (\frac{ \Delta P}{\Delta h})^2 $$

Rearranging:
$$u_c^2(\Delta P) = \Delta P^2  \left( (\frac{u(g) }{g})^2+
(\frac{u(\rho)}{\rho})^2+
 (\frac{ u(\Delta h)}{\Delta h})^2 \right)$$

$$u_c^2(\Delta P) = 114.3758^2  \left( (\frac{0.03}{9.80})^2+
(\frac{0.5}{1061})^2+
 (\frac{0.00141}{0.011})^2 \right)$$

$$u_c^2(\Delta P) = 215.06 Pa ^2$$
$$u_c^2(\Delta P) = 14.665 Pa$$

Now we know our uncertainty, we can round off to the
nearest 10 if our uncertainties are 1sf (we round up here
to be conservative)
$$\Delta P = 110 \pm 20 Pa$$

Or if we want 2sf uncertainty,

$$\Delta P = 114 \pm 15 Pa$$

Thus,
for even the simplest expression, there is quite some effort required
uncertainty
calculation to do. For complex systems, we can see that this
becomes quite tedious. Sometimes, these errors are correlated and then
we'll need to factor that into uncertainty calculations as well.
How can we automate this process?



Enter metrolopy. Run nodemon or python3 on the file with metrolopy
installed.


## notes on therminol

Heat Capacity Uncertainties can be found:

```
Gomez, Judith C., Greg C. Glatzmaier, and Mark 
Mehos. Heat capacity uncertainty calculation for 
the eutectic mixture of biphenyl/diphenyl ether 
used as heat transfer fluid. No. NREL/CP-5500-
56446. National Renewable Energy Lab.(NREL), 
Golden, CO (United States), 2012.
```
