
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = v1 + 3 
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6


# Initializing the model and the input tensors
m = Model()
 
x1 = torch.randn(20, 3, 64, 64) # Generate an input tensor of size (20, 3, 64, 64).
