
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 3)

    def forward(self, x):
        v1 = torch.nn.functional.linear(x, self.linear.weight, self.linear.bias)
        return v1.permute(0, 2, 1)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 2)
