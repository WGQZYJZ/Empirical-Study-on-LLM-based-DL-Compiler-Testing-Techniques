
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 2 or 3 representing the dimension of X (e.g., 2D image).
        self.bn  = torch.nn.BatchNorm2d(...)

    def forward(self, x):
        conv_input = self.conv(x)
        bn_output = self.bn(conv_input)

        return bn_output


# Inputs to the model
