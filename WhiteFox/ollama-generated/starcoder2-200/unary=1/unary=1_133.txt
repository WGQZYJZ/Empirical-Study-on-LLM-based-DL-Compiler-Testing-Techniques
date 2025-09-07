
m = nn.Sequential(
    nn.Linear(32 * 64 ** 2 , 1), 
    nn.Tanh(), 
    nn.ConstantPad1d((0, 0,), 1) # Add 1 to the output of the hyperbolic tangent function
    )

# Inputs to the model