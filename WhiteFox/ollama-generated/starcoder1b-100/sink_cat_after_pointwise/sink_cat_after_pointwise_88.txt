
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        # t0 and t1 are reshaped along a dimension
        t0 = torch.cat([x1, x1], dim=0).view(-1, 6)
        t1 = torch.relu(t0)
        # Output is concatenated along the last axis of `t0` and then passed through linear layer
        t2 = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 2)
