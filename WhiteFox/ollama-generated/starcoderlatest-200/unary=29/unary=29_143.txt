
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 8, 64, 64)
 min_value = torch.rand(1).mul_(1e-2)
 max_value = torch.rand(1).add_(1e-2)
 