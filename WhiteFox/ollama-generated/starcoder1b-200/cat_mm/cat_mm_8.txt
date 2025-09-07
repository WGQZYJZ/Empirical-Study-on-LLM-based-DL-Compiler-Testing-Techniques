
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = self.conv(x1)  # Pointwise convolution of two input tensors
        v2 = torch.cat([v1, v1], dim=0)  # Concatenation of the results of two pointwise convolutions along dimensions of `dim`
        return v2


# Inputs to the model
input1 = torch.randn(3, 4, 16, 16)
input2 = torch.randn(3, 4, 16, 16)
