
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)

    def forward(self, x1):
        v0 = x1 + other
        return torch.relu(v0)


m = Model()

# Initializing model with random inputs/tensors
x1 = torch.randn(237598763)
other = torch.randn(43, 87)
__output__  = m(x1)


