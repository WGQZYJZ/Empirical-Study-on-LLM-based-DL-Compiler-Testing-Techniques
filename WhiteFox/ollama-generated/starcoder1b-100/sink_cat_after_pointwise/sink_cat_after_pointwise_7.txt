
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.linear = ...  # Pre-trained linear layer

    def forward(self, x1):
        return self.linear(x1)


# Inputs to the model
x1 = torch.randn(3, 2, 4)
