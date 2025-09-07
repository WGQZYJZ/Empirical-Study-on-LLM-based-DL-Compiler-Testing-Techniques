
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = F.sigmoid(v1) # Use the PyTorch API for sigmoid
        v3  = v1 * v2 # Use PyTorch API for multiplication 
        return v3


# Initializing the model