
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.0):
        super().__init__()
        self.t = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = self.t(x1)
        t2 = torch.clamp_min(t1, min_value=min_value)
        t3 = torch.clamp_max(t2, max_value=max_value)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
