
class Model(torch.nn.Module):
    def __init__(self, max_value=128):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4)
        self.max = torch.Tensor([max_value]).float()
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, 0).clamp(max=self.max)
        return v2


# Initializing the model
m  = Model(48.356937731515315)


# Inputs to the model
x1  = torch.randn(1, 3, 10, 10)
__output__  = m(x1).clamp_max(m.max)

