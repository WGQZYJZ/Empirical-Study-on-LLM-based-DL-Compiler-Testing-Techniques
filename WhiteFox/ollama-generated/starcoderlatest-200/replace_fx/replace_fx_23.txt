 2
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5)
        v2 = torch.rand_like(v1)
        v3 = torch.cat((v2, v2), dim=1)
        v4 = torch.max(v3, 1)[0]
        v5 = self.linear(v4).unsqueeze(-1) # Unsqueeze the unsqueezed tensor for broadcasting purposes
        return v5


# Inputs to the model
x1 = torch.randn(2, 2, 2)
