
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)

        # Note: the two input tensors are passed in reverse order to `torch.bmm` or `torch.matmul`. The order is fixed in PyTorch.
        t3 = torch.bmm(v1, v2)
        t4 = torch.matmul(v1, v2)
        return [t3, t4]


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
