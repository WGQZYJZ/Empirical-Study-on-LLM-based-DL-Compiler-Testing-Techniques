

class Model(torch.nn.Module):
    def __init__(self, minv=None, maxv=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1): 
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min_value) if isinstance(min_value, float) else torch.clamp_min(v1, *min_value)
        v3  = torch.clamp_max(v2, max_value) if isinstance(max_value, float) else torch.clamp_max(v2, *max_value)
        return v3


# Initializing the model with keyword arguments for clamping operations.

m  = Model(minv=(-100,-5), maxv=(5,None)) # m(x1) will apply a clamp operation to the output of the convolution at both min and max values (-100 and -5 respectively) as well as (5 and infinite respectively).


m  = Model() # Applying no clamping operation.

# Inputs to the model.
__output__  = m(x1)



