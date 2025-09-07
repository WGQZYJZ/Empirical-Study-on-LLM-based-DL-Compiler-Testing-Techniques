
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2, bias=True)

    def forward(self, x1):
        # Perform the linear transformation and clamp to [0, 6]
        l1 = self.linear(x1)
        l2 = l1 * clamp(min=0, max=6, l1 + 3)
        l3 = l2 / 6  # Divide by 6

        return l3
