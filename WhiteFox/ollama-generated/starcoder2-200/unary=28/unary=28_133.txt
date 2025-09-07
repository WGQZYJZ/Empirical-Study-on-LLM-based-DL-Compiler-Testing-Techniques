
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=-0.5) # -0.5 is provided as keyword argument
        v3 = torch.clamp_max(v2, max=7.0) 
        return v3

m  = Model()
x1 = torch.randn(4, 32)
