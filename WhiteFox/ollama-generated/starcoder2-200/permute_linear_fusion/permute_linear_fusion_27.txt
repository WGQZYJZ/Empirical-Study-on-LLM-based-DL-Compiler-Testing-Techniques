
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v3 = torch.nn.functional.linear(x1, self.linear.weight) # The modified input tensor should not contain the self.linear.bias term.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn(1, 4)
__output__  = m(x2)
