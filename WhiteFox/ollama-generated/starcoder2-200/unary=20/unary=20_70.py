
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v0 = x1 
        v1  = self.deconv(v0)
        v2  = torch.sigmoid(v1)
        return v2

# Initializing the model