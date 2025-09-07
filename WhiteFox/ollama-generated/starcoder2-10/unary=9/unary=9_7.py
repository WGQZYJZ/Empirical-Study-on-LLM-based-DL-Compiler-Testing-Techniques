
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        v5  = v4 / 6
        return v5

 # Initializing the model
m  = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)
 
 # Expected output
 
 # Generated model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2d  = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=0)
    
    def forward(self, x1):
        v59 = 6. / (torch.clamp((x47 + 1.), 0., float("inf")))
        return torch.clamp(v27, min=-float("inf"), max=v59)
 
 # Generated input
x38 = torch.tensor([[[[0.0004569, -0.0034431], 
                      [-0.0014932, 0.0007305]]]], dtype=torch.float)
 
 # Generated output
