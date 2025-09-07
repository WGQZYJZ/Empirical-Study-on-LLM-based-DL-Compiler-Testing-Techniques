

class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, kwargs["min"])
        v3  = torch.clamp_max(v2, kwargs["max"])
        return v3

# Initializing the model with keyword arguments and specifying the minimum value to clamp at `0` as well as a maximum value of `1`. Note that since keyword arguments are passed in the forward method call (`kwargs`), these values will be dynamic.
m  = Model(min=0, max=1)

 # Inputs to the model:
x1  = torch.randn(432, 576)
__output__  = m(x1)
 

# Please specify the arguments and values of `max_value` and `min_value`. The minimum value can also be negative (`-0.8`) for this example.
 
