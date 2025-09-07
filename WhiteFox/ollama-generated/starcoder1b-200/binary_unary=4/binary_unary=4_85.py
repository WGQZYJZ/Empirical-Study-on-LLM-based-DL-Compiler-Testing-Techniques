
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1: Tensor, other=None):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other
        else:
            v2 = v1
        return relu(v2)


# Initializing the model
m = Model()
other = torch.randn((2, 3))
