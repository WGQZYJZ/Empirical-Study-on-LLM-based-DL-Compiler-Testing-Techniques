
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1)
 
    def forward(self, x1, min_value=0.0, max_value=1.0):
        v1 = self.conv_transpose(x1, min_value=min_value, max_value=max_value)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
