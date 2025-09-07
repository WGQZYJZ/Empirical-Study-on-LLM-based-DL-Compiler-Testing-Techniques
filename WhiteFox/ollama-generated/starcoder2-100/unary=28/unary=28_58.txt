
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-32, max_value=0.5):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_value)
        v3  = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with min value as -5 and max value as 0.8
m = Model(-5., 0.8)

# Inputs to the model
x1 = torch.randn(1,4 )
 
__output__  = m(x1)
