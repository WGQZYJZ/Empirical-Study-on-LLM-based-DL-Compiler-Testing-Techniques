
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1, min_value=0, max_value=1):
        v1 = self.conv_transpose(x1, min_value=min_value, max_value=max_value)
        return v1

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
