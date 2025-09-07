
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 3)

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.linear1.weight) # Input tensor after conv layer is passed through the weight matrix of the convolution layer with stride=2 and padding=0
        v2 = torch.nn.functional.linear(v1, self.linear2.weight, self.linear2.bias)  # Apply linear transformation on the permuted tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 5, 10, 14)
