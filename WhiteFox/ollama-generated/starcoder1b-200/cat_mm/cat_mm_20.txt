
class Model(torch.nn.Module):
    def __init__(self, input_shape):
        super().__init__()
        self.conv = torch.nn.Conv2d(*input_shape, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.cat([v1, v1, v1, ...], dim=-1)


# Inputs to the model
m = Model((3, 64, 64))
input_tensor = torch.randn(*shape, 3)
