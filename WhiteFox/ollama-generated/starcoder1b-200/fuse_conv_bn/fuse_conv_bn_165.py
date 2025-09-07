
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # X can be 1, 2 or 3 representing the dimension. 
        x2  = conv_bn(x1, 1)
        return torch.nn.functional.linear(x2, self.linear.weight, self.linear.bias)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
