
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.deconv(x1)
        v2  = v1 > 0
        v3  = v1 * -4.57908e-06
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 57, 57)
