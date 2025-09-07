
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.leaky = torch.nn.LeakyReLU(negative_slope)
 
    def forward(self, x1): 
        v1 = self.conv(x1)
        v2 = v1 > 0  
        v3 = negative_slope * v1   # Replace the constant with a hyperparameter named negative_slope
        v4 = torch.where(v2, v1, v3)

        return v4


# Initializing the model
negative_slope=0.5
m = Model(negative_slope)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)


