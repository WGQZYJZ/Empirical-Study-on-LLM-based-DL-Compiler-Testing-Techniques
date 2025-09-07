
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn = torch.nn.BatchNormXd(...)  # X should match with ConvXd
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()
m.__set_trainable__()  # Set trainable model to non-trainable.

# Inputs to the model
x1 = torch.randn(3, 4, 5)
