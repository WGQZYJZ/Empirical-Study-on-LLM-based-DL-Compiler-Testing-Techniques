
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1) * 10
        v2 = torch.nn.functional.dropout(v1, p=0.5) # Apply dropout to the random tensor
        v3 = self.linear(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
