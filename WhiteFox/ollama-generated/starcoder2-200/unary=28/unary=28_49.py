
class Model(torch.nn.Module):
    def __init__(self, minv=0., maxv=1):
        super().__init__()
        self.conv  = torch.nn.Linear(84 * 32 + 3, 6)
 
    def forward(self, x1):
        v1   = torch.randn(x1.shape[0], 72*85, 3).to(device=device, dtype=torch.float32),
        v1_  = self.conv(v1)
        v2  = torch.clamp(v1_, minv, maxv)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model: 
x1 = torch.rand(3795408).view(-1, 376, 85)
__output__  = m(x1)

