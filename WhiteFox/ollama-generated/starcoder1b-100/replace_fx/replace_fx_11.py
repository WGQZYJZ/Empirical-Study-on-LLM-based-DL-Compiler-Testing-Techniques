
class Model(torch.nn.Module):
    def __init__(self, fallback_random=False):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        if not self.training and self._fallback_random:
            return torch.nn.functional.dropout(input_tensor, 0)
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 2, 2)
