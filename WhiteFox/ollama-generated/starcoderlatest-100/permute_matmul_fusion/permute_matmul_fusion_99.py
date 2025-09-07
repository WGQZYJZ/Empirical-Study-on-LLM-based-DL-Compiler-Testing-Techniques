
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Swap the last two dimensions of A and B
        v2 = x2.permute(0, 2, 1)
        v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4)
x2 = torch.randn(1, 4, 2)
