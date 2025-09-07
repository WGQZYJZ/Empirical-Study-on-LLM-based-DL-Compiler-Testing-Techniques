
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.)
        return torch.clamp_max(v2, max=5., inplace=True)
# Initializing the model with a custom minimum value of `0` and a maximum value of `5`.
m  = Model()
