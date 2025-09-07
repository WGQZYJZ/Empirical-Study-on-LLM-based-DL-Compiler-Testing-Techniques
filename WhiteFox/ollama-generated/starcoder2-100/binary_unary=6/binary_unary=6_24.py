
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v0 = torch.randn(5, 3).requires_grad_(True)
        v2 = self.linear1(x1)
        v4 = other + v0 - 7 # some other value
        v6 = relu(v2 - v4) 
        return v6


# Initializing the model and running it on an input tensor x1 of shape (5, 3).
m = Model()
x1 = torch.randn((5, 3))
v10 = m(x1)

