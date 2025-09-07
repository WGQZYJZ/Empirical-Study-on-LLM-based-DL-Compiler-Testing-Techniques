
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=None):
        super().__init__()
        self.linear  = torch.nn.Linear(4096, 128)

    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.clamp_min(v1, min=min_value) # Clamp the output of the linear transformation to a minimum value
        v3  = torch.clamp_max(v2, max=max_value) # Clamp the output of the previous operation to a maximum value 
        return v3

# Initializing the model
minval  = -10569347.81007753
maxval  =  10892323.740599416
m  = Model(min_value=minval, max_value=maxval)

# Inputs to the model
x1  = torch.randn(4, 128)
__output__  = m(x1)

