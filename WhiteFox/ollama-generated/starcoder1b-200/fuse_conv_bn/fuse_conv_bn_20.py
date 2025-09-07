
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        x2 = torch.nn.functional.conv2d(x1, self.linear.weight, self.linear.bias, ...) # X can be 1, 2, or 3 representing the dimension
        return ...


# Initializing the model
m = Model()


