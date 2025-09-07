
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear1.weight, self.linear1.bias)
        v4 = v3.permute(0, 2, 1)

        return v4

# Initializing the model