
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.conv  = torch.nn.Linear(3*64**2, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1.reshape(-1))
        v2 = torch.clamp_min(v1, min_)
        v3 = torch.clamp_max(v2, max_)
 
        return v3


# Initializing the model
m  = Model(0., 1.)

# Inputs to the model
x1 = torch.randn(49, 8)
__output__  = m(x1)

