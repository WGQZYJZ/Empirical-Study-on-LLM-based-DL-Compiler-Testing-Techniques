
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = x1
        v1 = F.linear(v0, torch.ones(x1.shape[1]))
        v5 = F.clamp_max(F.clamp_min(v1, min=-2), max=3) # 6th line of Model class
        return (v5, x1[:, :int(x1.shape[1]/2)])
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(80, 16, 4)

