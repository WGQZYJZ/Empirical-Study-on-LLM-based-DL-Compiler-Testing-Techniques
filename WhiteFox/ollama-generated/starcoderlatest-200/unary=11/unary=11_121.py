
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) + 3
        v2 = torch.clamp(v1, min=0.0)
        v3 = torch.clamp(v2, max=6.0)
        return v3 / 6


# Generating example with the model (15 iterations)
from pytorch_model_summary import summary
for _ in range(15):
    summary(m, input_size=(1, 3, 64, 64))

    x1 = torch.randn(1, 3, 64, 64).float()
    