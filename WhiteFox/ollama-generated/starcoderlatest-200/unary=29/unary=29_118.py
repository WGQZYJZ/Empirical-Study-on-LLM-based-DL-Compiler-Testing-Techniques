
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0.5, max_value=0.7071067811865476):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp(v1 * 0.5, min_value, max_value)
        v3 = torch.clamp(v2 * 0.7071067811865476, min_value, max_value)
        return v3

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
