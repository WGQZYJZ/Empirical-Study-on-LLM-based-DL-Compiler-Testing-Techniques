
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.relu(v2)
        v4  = torch.clamp_max(v3, 6) / 6
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 50, 80)
__output__  = m(x1)
 
