
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Randomly replace input to the linear transformation with a tensor
        t2 = torch.rand_like(x1, 0.25, dtype=x1.dtype)
        v1  = torch.nn.functional.dropout(t2, self.linear.weight, self.linear.bias)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Inputs to the model
x1  = torch.randn(1, 2, 2)
