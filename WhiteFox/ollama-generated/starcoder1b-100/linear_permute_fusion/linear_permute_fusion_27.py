
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.tensor([[0., 0.], [1., 0.], [1., 1.]])
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

# Inputs to the model
x1 = torch.randn(1, 2, 2)
