
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)

    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 28 * 28))
        v2 = torch.clamp_min(v1, min=-60.53982543945312)
        v3 = torch.clamp_max(v2, max=70.830322265625)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
__inputs__  = [torch.randn(1, 28 * 28)]

