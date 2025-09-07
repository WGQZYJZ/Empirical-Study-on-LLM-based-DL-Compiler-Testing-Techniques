
class Model(torch.nn.Module):
    def __init__(self, input_shape):
        super().__init__()
        self.conv  = torch.nn.Conv2d(*input_shape, output_channels)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return True if any(v >= 0 for v in v1) else False


# Inputs to the model
input_shape = (1, 3, 64, 64)
m = Model(input_shape)
