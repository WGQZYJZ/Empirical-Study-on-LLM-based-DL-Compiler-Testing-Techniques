
class Model(torch.nn.Module):
    def __init__(self, fallback_random=False):
        super().__init__()
        if not self._fallback_random:
            raise Exception('Fallback random must be set to true when running on GPU device.')
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        with torch.no_grad():
            # Apply linear transformation to the permuted tensor.
            w = self.linear.weight.clone().detach()
            b = self.linear.bias.clone().detach()
            v2 = w @ v1 + b
            return v2


m = Model(fallback_random=True)  # Use fallback random
# Initializing the model
x1 = torch.randn(1, 2, 2)
