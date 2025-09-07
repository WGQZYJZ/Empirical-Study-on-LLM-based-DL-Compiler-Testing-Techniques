
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 2, 3)
        self.bn = torch.nn.BatchNorm2d(2)

    def forward(self, x1):
        # Please write the model code here to meet the specified requirements
        output = self.bn(self.conv(x1))

        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 4)
