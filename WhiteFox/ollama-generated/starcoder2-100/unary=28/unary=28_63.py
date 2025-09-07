
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=-0.9)
        v3 = torch.clamp_max(v2, max=10.)
        return v3


# Initializing the model with provided keyword arguments: `min` and `max`
m  = Model(min=-0.5, max=4.768371582031)
 
# Inputs to the model
x1 = torch.randn(1, 5)
__output__  = m(x1)

