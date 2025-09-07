
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1.permute(0, 2, 1), self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
__inputs__ = {'x': torch.randn(3, 3, 4)}