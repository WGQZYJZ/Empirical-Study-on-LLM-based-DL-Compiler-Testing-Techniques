
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=1, padding=0)
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x): # The forward pass for the network 
        v1 = self.convt(x)
        mask  = v1 > 0
        v2 = v1 * -5
        v3 = torch.where(mask, v1, v2)
        return v3


# Initializing model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # A 3 channel image of shape (3, 64, 64).
__output__  = m(x1)

