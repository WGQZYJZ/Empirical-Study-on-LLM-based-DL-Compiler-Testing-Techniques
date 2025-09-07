
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3)

    def forward(self, x1):
        bn = torch.nn.functional.batch_norm(...)
        output = self.conv(bn(x1))

        return output


# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
