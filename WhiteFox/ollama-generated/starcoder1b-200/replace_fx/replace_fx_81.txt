
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        with self.fallback_random():
            v1 = x1.permute(0, 2, 1)
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)


