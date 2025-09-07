
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, 5)

    def forward(self, x1):
        bn = torch.nn.BatchNorm2d(x1.shape[1])

        # Functional pattern (torch.nn.functional.*)
        output = bn(torch.nn.functional.conv2d(x1, self.conv))
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 1, 5, 5)
