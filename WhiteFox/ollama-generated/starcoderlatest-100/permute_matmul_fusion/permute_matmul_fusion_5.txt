
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight)
        v2 = torch.nn.functional.linear(x2, self.linear2.weight)
        v3  = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 16, 16)
x2 = torch.randn(1, 16, 16)
