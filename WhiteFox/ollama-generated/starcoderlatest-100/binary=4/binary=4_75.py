
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        if other:
            self.other = torch.nn.Parameter(
                torch.rand_like(other), requires_grad=True
            )
 
    def forward(self, x1):
        v1 = self.linear(x1) + (
            None if self.other is None else self.other
        )
        return v1


# Initializing the model with "other" tensor as an input
m = Model()
x2 = torch.randn(1, 3, 64, 64)
v = m(x2)

