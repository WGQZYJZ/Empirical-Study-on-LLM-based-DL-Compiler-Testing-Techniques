
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5, max=1)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(4,3,8,9)
 
# Executing the model and obtaining the output
