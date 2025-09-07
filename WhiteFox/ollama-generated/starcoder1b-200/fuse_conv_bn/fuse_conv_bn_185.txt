
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)  # X can be 1, 2 or 3 representing the dimension of input tensor.
        self.bn   = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        out  = self.conv(x)
        out  = self.bn(out)
        return out


# Inputs to the model
input_tensor  = ...  # Permute the input tensor first
__output__   = Model().forward(input_tensor)


