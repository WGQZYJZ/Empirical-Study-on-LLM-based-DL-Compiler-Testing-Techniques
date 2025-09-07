
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp_min(v1, min=0) # Clamp the output of the transposed convolution to a minimum value (0 in this example)
        return torch.clamp_max(v2, max=5)

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
  __output__   = m(x1)

