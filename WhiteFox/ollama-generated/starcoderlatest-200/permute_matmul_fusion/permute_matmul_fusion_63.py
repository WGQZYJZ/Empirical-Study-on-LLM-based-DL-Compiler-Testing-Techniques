
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias).permute(0, 2, 1)
        v2 = torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias).permute(0, 2, 1)
        return torch.bmm(v1, v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4, requires_grad=True)
x2 = torch.randn(1, 2, 3, requires_grad=True)
