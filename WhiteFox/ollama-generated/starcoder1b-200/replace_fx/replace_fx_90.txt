
class Model(torch.nn.Module):
    def __init__(self, optimizer: torch.optim.Optimizer = None):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)
        self.optimizer = optimizer

    def forward(self, x1, **kwargs):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(torch.rand_like(input_tensor), p=0.5)
        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v3


# Initializing the model
m = Model()
optim = torch.optim.SGD(m.parameters(), lr=0.2, momentum=0.5)
m.optimizer = optim  # Note that `m.optimizer` is used to access the optimizer inside `m`, not as an argument.

# Inputs to the model
x1 = torch.randn(1, 2, 2)
