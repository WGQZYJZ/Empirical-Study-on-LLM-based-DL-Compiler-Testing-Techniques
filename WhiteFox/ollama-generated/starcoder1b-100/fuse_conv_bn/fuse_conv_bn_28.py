
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        output = torch.nn.functional.conv2d(input_tensor, self.conv.weight, self.conv.bias) # X can be 1, 2 or 3 representing the number of dimensions
        return output


# Inputs to the model
x1 = torch.randn(1, 2, 2)
