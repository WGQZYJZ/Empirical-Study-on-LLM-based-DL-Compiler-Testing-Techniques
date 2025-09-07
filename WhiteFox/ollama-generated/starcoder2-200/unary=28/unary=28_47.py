
class Model(torch.nn.Module):
    def __init__(self, max_value=10., min_value=-2.5):
        super().__init__()
        self.linear  = torch.nn.Linear(3,8)
 
    def forward(self, x):
        v1  = self.linear(x) 
        v2  = torch.clamp_min(v1, max=max_value) 
        v3  = torch.clamp_max(v2, min=min_value) 
        return v3


# Initializing the model with default values for the minimum and maximum values of clamping.
m  = Model()

 # Inputs to the model
x1 = torch.randn(10, 3)
 
# Computing the output using the model inputs.
__output__  = m(x1)

