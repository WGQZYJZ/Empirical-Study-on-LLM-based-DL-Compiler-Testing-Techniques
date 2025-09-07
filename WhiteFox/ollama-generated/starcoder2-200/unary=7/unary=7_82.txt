
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)

    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = l1 * nn.functional.clamp(min=0, max=6, x=l1 + 3)
        l3 = l2 / 6
        return l3


# Initializing the model