
class Model(torch.nn.Module):
    def __init__(self, fallback_random=False):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        if not self.training:
            self._fallback_random(v1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

    def _fallback_random(self, x):
        # Generate a random number
        x[...]  = torch.randint(0, 2 ** (x.dim() - 2), [2] + list(x.shape)[1:])
