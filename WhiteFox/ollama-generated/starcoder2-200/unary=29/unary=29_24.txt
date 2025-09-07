
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.clamp_min(v1, min(-67)) # Here we use -67 as an example for the minimum value of the clamp operation to meet the specific requirements.
        v3  = torch.clamp_max(v2, max(50)) 
        return v3


# Initializing model and inputs to model
m  = Model()
x1  = torch.randn(1, 8, 64, 64)
__output__  = m(x1)