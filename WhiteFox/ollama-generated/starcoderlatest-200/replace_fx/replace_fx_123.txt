
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.rand_like(x1, dtype=torch.float32)
        v2 = torch.nn.functional.dropout(v1, p=0.5)
        return self.linear(v2)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
