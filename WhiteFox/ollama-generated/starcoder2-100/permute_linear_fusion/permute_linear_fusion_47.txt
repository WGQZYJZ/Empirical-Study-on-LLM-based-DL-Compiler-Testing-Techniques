
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.nn.functional.linear(x1.permute(0, 3, 1), self.linear.weight) # swapping 2-D to 4-D here is ok

        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 2, 3)
