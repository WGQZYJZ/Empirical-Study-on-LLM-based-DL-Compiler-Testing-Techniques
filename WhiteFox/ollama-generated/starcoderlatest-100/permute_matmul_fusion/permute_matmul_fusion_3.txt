
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.bmm(x1, x2) # (1, 2, 2) @ (2, 2, 2) = (1, 2, 2) 
        v2 = torch.matmul(x1, x3) # (1, 1, 3) @ (1, 3, 2) = (1, 1, 2)
        return v1 + v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
x3 = torch.randn(1, 1, 2)
