
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = torch.clamp_min(v1, min_value=-0.5)
        v3  = torch.clamp_max(v2, max_value=64.0) # Clamp the maximum value is fixed to `64`. 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 1, 2) + 5


