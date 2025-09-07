
class Model(torch.nn.Module):
    def __init__(self, min_value = 1, max_value = 5):
        super().__init__()
        self.conv_tr  = torch.nn.ConvTranspose2d(3, 3, 6, stride=6, padding=0)

    def forward(self, x1):
        v1 = self.conv_tr(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
