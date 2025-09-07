
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other): # This model is different from the previous one.
        v1 = self.conv(x1) 
        v2 = v1 + other
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # The input tensors are passed as positional arguments.
other = torch.randn(8, 50, 27, 39) 

__output__= m(x1, other)

