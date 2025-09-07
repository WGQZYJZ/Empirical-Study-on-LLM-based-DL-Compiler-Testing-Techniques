
class Model(torch.nn.Module):
    def __init__(self, max_value=100):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=(2, 2), stride=(1, 1), padding=(0, 0))
        self.max_value = max_value
 
    def forward(self, x):
        v = self.conv_transpose(x)
        v = torch.clamp_min(v, min_value=self.max_value - 1)
        v = torch.clamp_max(v, max_value=self.max_value + 1)
        return v


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
