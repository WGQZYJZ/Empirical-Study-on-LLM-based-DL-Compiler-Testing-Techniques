
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return torch.bmm(x1, x2)  # or torch.matmul(x1, x2)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 3, 4)
x2  = torch.randn(4, 2, 3, 5)
