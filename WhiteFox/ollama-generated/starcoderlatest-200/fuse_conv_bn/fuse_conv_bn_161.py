
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension

    def forward(self, x):
        conv_out = self.conv1(x)
        bn_out   = ...  # batch norm with input from conv

        return bn_out


# Inputs to the model
x1 = torch.randn(1, 2, 2)
