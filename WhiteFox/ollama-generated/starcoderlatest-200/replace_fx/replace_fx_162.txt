
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.25) # Replace the dropout function
        v2 = torch.rand_like(x1)  # Don't replace this function
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
