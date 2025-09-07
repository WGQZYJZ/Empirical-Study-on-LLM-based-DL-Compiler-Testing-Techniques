
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.conv2 = torch.nn.ConvXd(...)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.conv_transpose2d(...)(v1)  # X should match with ConvXd
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 6, 8)
