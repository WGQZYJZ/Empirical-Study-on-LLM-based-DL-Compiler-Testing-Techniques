
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 2)

    def forward(self, x1):
        # No batch normalization in this model
        output = torch.nn.functional.conv2d(x1, self.conv.weight, bias=self.conv.bias, stride=1, padding=0)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 3, 2)
