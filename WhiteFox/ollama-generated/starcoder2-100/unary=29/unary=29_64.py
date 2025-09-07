
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v0 = torch.tensor([min_value])
        v1  = self.conv(x1) 
        v4 = v1 > v0[None, None, :, :]
        v2 = torch.clamp(v1, min=v0).float()
        v3 = torch.clamp(v2, max=max_value).float()
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)