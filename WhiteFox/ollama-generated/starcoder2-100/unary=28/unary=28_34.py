
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min=0) # Clamp the output of the linear transformation to a minimum value equal to zero 
        v3  = torch.clamp_max(v2, max=-5) # Clamp the output of the previous operation to a maximum value equal to -5
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(10000, 1024)
__output__  = m(x1)

