
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1).view(-1, 8)
        v2 = torch.relu(v1.t().contiguous())
        return v2

# Inputs to the model
x1 = torch.randn(1, 2, 4, 8)
