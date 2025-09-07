
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.bmm(x1.permute(0, 2, 1), x2) #or torch.matmul(x1, x2)
        v2 = torch.bmm(x2.permute(0, 2, 1), x1) #or torch.matmul(x2, x1)
        return v1+v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 3, 2)
