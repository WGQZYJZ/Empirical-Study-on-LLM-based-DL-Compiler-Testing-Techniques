
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 28*28))
        v2 = v1 + other_tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 1, 64, 64)
