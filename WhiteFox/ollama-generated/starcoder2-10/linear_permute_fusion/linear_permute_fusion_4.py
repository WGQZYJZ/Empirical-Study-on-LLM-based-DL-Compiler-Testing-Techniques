
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, weight=self.linear.weight, bias=self.linear.bias) # pylint: disable=not-callable
        return v1

# Initializing the model