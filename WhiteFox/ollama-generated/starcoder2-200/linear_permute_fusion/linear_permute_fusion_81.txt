
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 3)

    def forward(self, x):
        return torch.nn.functional.linear(x, self.linear1.weight)
