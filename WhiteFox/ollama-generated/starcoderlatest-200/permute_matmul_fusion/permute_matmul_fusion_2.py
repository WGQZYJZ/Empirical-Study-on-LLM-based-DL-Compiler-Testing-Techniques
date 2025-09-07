
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2) # or torch.matmul(t1, t2)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 3)
x2 = torch.randn(3, 3, 2)
