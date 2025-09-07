
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 3)
        self.linear_B = torch.nn.Linear(4, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear_A.weight, self.linear_A.bias)
        v3 = x2.permute(0, 2, 1)
        v4 = torch.nn.functional.linear(v3, self.linear_B.weight, self.linear_B.bias)

        # The permute functions above could have been replaced by bmm or matmul below, but it is not shown here for brevity reasons.
        t1 = torch.bmm(v2, v4)
        return t1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 4, 3)
