
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, -96)
        v3  = torch.clamp_max(v2, 72.8)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4096, 3, 35, 35)
