
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm((None, None))
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        x1 = self.layer_norm(x1)
        v1 = self.conv(x1)
        return v1

# Inputs to the model
input_tensor = torch.randn((3, 8, 64, 64), requires_grad=True)
