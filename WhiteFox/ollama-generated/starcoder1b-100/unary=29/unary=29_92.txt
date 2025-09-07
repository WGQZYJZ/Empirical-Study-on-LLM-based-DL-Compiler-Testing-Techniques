
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1, min_value=-1e9, max_value=1e9):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Inputs to the model
__input__ = torch.randn(1, 8, 64, 64)
__output_with_clamp__, __output_without_clamp__ = Model()(__input__)


