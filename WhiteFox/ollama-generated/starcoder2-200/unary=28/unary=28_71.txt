

class Model(torch.nn.Module):
    def __init__(self, maxv=0., minv=-1., **kwargs)
        super().__init__()
        self.linear = torch.nn.Linear(**kwargs)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to input tensor
        v2  = torch.clamp_min(v1, min=mimv) # Clamp output of the linear transformation to minimum value
        v3  = torch.clamp_max(v2, max=maxv) # Clamp output of previous operation to maximum value
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 100)
