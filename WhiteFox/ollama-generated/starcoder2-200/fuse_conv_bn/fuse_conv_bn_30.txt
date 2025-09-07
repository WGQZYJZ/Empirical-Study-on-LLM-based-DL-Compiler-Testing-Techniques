
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v  = torch.nn.functional.conv2d(x1, weight=None) # The first arg of conv2d must be input tensor
        return v


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(5, 3000, 4, 96871)

# Output from the model
__output__  = m(input_tensor)

