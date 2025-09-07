
class Conv2d:
    def __init__(self):
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.nn.functional.conv2d(x1, self.linear.weight, self.linear.bias, self.linear.stride, self.linear.padding)

# Initializing the model
conv = Conv2d()


