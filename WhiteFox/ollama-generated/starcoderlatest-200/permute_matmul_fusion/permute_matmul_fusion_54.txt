
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x1.permute(0, 2, 1))
        v2 = torch.matmul(v1, x1.permute(0, 2, 1).transpose(0, 1)) # Use the permuted tensors to invoke `torch.bmm` or `torch.matmul`.
        v3 = torch.matmul(x1, x1)
        return self.linear(v1), self.linear(v2), self.linear(v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4)
x2 = torch.randn(1, 3, 4)
