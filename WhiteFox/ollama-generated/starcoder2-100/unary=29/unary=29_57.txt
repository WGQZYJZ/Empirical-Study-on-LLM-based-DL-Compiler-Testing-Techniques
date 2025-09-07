
class Model(torch.nn.Module):
    def __init__(self, min_value=-10, max_value=42):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 3, stride=1)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with keyword arguments
m  = Model(min_value=-50, max_value=67894)

 # Inputs to the model
    x1  = torch.randn(1, 3, 32, 32)
__output__  = m(x1)