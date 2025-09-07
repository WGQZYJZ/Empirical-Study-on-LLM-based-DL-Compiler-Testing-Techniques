
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-4, max_value=30.5):
        super().__init__()
        self.conv_transposed = torch.nn.ConvTranspose2d(64, 3, 2, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_transposed(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model()

