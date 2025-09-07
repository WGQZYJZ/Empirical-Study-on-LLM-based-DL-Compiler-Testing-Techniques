
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.clamp_min(v1, -0.5)
        return torch.clamp_max(v2, 0.9)

m  = Model()


x1  = torch.randn(1, 3, 64, 64) # Input to the model (of shape 1 x 3 x 64 x 64)
__output__  = m(x1)

