
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear1(x1) + 3 # Applying a linear transformation to an input tensor
        v2  = torch.clamp_min(v1, 0.)
        v3  = torch.clamp_max(v2, 6.)
        v4  = v3 / 6.
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1) # Applying the linear transformation to an input tensor
__output__  = m(x1)