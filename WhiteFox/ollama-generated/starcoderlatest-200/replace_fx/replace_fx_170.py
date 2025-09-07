
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, ...).permute(...).contiguous() # Generate a permuted tensor from the input tensor
        v2 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
