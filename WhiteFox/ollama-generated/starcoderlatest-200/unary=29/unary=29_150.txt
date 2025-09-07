
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1, min_value=0, max_value=255):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp(v1, min=min_value, max=max_value)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
