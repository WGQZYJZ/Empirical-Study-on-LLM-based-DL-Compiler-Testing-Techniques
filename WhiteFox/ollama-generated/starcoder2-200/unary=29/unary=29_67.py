
class Model(torch.nn.Module):
    def __init__(self, max=10, min=-5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 3)
    
    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, min=-500.) # clamp_min = -5 is in the original text
        return torch.clamp_max(v2, max=5.) # clamp_max = 5 is in the original text
 

m  = Model()

 # Input to the model
x1  = torch.randn(1, 3, 84, 84)

__output__  = m(x1)
 