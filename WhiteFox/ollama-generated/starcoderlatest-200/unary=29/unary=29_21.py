
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        min_value = -2
        max_value = 6
        t2 = torch.clamp_min(v1, min_value)
        t3 = torch.clamp_max(t2, max_value)
        return t3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
