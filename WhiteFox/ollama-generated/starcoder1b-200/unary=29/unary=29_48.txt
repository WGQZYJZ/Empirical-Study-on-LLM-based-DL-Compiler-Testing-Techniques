
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value, max_value):
        v1 = self.conv_transpose(x1, min_value, max_value)
        return v1


# Inputs to the model
input_tensor  = torch.randn(1, 8, 64, 64)
min_value    = 0.
max_value    = 5.
__output__   = m(input_tensor, min_value, max_value)

