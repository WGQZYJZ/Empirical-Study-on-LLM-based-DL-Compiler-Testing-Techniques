
class Model(torch.nn.Module):
    def __init__(self, min_value=-20.0, max_value=3458679.123):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = torch.clamp_min(v1, -20.0)
        v3  = torch.clamp_max(v2, 3458679.123)
        return v3


# Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

