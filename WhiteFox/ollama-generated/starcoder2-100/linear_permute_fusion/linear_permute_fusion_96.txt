
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 1)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)
        v2 = v1.permute(-1, -2)
        return v2


# Initializing the model