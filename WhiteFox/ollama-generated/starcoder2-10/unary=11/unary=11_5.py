

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
    
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        return v4 / 6

m  = Model()
x1  = torch.randn(1, 8, 512, 512) # Shape of input tensor to be fed into the model
__output__  = m(x1)

