
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # permute input tensor A
        v2 = x2.permute(0, 2, 1) # permute input tensor B

        v3 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        v4 = torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias)

        return torch.bmm(v3, v4) # or torch.matmul(v3, v4)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
