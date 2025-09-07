
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) > 0
        v2  = -v1 + (torch.rand_like(v1) < negative_slope) * v1  # Note that we don't actually use the `torch.rand_like` method; we just add it to make it clearer which part of the calculation depends on `negative_slope`.
        v3  = torch.where(v2, v1, v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model