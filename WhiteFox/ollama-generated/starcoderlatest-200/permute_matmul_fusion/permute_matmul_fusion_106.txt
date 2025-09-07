
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2)
        v2 = torch.matmul(x1, x2)
        v3 = torch.add(v1, v2)
        return self.linear(v3)


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 3, 2)
