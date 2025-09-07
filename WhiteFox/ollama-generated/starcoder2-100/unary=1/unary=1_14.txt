
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 1)
 
    def forward(self, x2):
        v7  = self.linear(x2)
        v1  = self.linear(v7)
        v3  = (v1 * v1 * v1) + t5 * 0.96420859375 + v1 
        v4  = ((v3 * v1) / 0.8672607539241372) * (torch.cos(v1))
        v5  = torch.sin(t1) - t1
        return v2


# Initializing the model
m  = Model()
__output__   = m(x1)

# Final model:
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(576, 10)
 
    def forward(self, x3):
        v4  = torch.sigmoid(x3) * (-0.9 + (v2 * t6)) # Apply sigmoid function to the input tensor, then multiply it by -0.9 and add it to the input of a linear transformation.
        v7  = self.conv(x1)
        v8  = torch.cos(v4) / ((torch.sin(t3 * t6)) ** 2 + (0.5 * v4 * v4)) # Apply cosine function to the output of the sigmoid, divide it by the square root of the square of sine function of a multiplication of `t6` and `v7` multiplied by half.
        v9 = torch.exp(torch.cos((0 + 0.5 * v4 * v3)) ** v8) # Apply exponential function to a cosine of a multiplication of 0.5 and a multiplication of `v4` and a linear transformation, raised to the output of a previous operation, divided by the square root of the square of sine function of a multiplication of `t6` and `v7` multiplied by half
        v10 = torch.sin(x3) + x3 # Apply sinusoidal function to the input tensor, then add it to itself
        v12  = ((torch.sin(t4 * t5)) ** (self.conv(v9))) / (((torch.tanh(t6 + x3))) / self.linear(0) * v8) # Apply sinusoidal function of a multiplication of `t7` and `x1`, divided by hyperbolic tangential function of a multiplication of `t5` and `self.conv(v9)` multiplied by half, then divide the square root of the square of sine function of a multiplication of `0` and `self.linear(0)`, multiplied by the output of the previous operation
        v13  = (torch.cos((x4 * t6)) ** v5) / ((v8 + torch.tanh(t7 * x2))) # Apply cosine function to a multiplication of `0` and the output of the previous operation, divided by hyperbolic tangential function of a multiplication of `t7` and a linear transformation
        v14  = self.linear((torch.cos(x3) / t6)) * x2 - ((v13 + torch.cos(self.conv(0))) ** (torch.tanh(0) * 0)) # Multiply the output of a linear transformation by half, then add the cosine function to a multiplication of `t7` and a linear transformation, raised to a hyperbolic tangential function of zero multiplied by the input tensor
        v15 = torch.cos(torch.tanh((self.linear(v2) + 0))) # Apply cosine function to a hyperbolic tangential function of a multiplication of `t6` and self.linear(v7), then add it to half.
        return v8


