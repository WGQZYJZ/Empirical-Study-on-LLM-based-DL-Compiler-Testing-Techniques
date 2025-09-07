
class Model(torch.nn.Module):
    def __init__(self, input_shape):
        super().__init__()
        self.linear = torch.nn.Linear(*input_shape)

    def forward(self, x1):
        return torch.relu(self.linear(x1))


# Inputs to the model
inputs = torch.randn(2, 3)
