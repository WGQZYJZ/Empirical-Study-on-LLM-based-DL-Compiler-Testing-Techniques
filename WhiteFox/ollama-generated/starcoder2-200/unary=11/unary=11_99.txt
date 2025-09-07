
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = v1 + 3
        v3 = F.relu6(v2).clamp(min=0, max=6) / 6
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 47, 47)

__output__  = m(x1)

