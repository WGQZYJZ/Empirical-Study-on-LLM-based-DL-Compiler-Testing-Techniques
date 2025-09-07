
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x1)
        v2 = torch.bmm(x2, x2) # or torch.matmul(x2, x2)
        v3 = torch.bmm(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2)
x2 = torch.randn(6, 2)
