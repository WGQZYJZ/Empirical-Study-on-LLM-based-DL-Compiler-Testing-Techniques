
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.nn.functional.conv2d(
            x1, self._weight, bias=None)


# Initializing the model 
m = Model()

# Inputs to the model 
input_tensor  = torch.randn(3, 8, 56, 56)

