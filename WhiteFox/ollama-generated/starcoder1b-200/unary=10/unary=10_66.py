
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = l1 + 3
        return torch.clamp_min(l2, 0), torch.clamp_max(l3, 6)


# Initializing the model
m = Model()


