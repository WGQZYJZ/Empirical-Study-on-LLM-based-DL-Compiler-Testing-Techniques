
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1)
    
    def forward(self, x):
      v1 = self.deconv(x1)
      return v1

# Initializing the model