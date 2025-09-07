
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        return (v4 / 6).float()

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1,8,5,7)# __output__  = m(x1)
