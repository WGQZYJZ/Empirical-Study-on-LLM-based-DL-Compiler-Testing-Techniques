
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1000, 5)

    def forward(self, x):
        v2  = torch.nn.functional.linear(x, self.linear.weight, self.linear.bias)
        v3  = v2.permute(-1, -2) # swap the two last dimensions of the permuted tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(456, 789)
__output__  = m(x).shape == [1000, 2]