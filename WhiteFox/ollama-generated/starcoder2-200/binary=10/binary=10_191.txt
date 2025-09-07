

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 10, 5)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + x2  # The argument "other" is assigned to be an input tensor of the same shape as the input tensor.
        return v2


m = Model()

x1 = torch.randn(30, 32 * 10)
x2 = torch.randn(30, 5) # The shapes of x1 and x2 must be compatible with each other according to the formula: [N, in_features] * [in_features, out_features]
