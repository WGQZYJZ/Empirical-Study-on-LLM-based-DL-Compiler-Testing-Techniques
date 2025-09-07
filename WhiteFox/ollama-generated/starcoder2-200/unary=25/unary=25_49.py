
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*32, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply a linear transformation to the input tensor
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3*1*1*4900)
