
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.full([12], 1, device=device)

    def forward(self, x1, arg2):
        v1 = self.full[arg2]
        return v1

# Inputs to the model
x1 = torch.randn(12, dtype=torch.float64)
