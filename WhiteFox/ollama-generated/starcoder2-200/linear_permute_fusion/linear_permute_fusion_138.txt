
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)

    def forward(self, x2):
        v2a = torch.nn.functional.linear(x2, self.linear1.weight)

        v3 = self.linear1(v2a).permute([0, 3, 1])
        return v3


# Initializing the model