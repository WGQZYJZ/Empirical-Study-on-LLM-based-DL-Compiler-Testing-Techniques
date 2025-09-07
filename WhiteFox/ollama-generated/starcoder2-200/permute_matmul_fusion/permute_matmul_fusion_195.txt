
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2) # or torch.matmul(v1, x2), but it is not supported by source-code analyzer.
        return self.linear(v2)

# Initializing the model
m = Model()


# Inputs to the model 1
x1A = torch.randn(5, 3, 4) # batch_size=5, 3 for dim0 is fixed.
__outputA__ = m(x1A)

# Inputs to the model 2
x1B = torch.randn(1, 1, 6) # batch_size=1, dim0 is fixed and equal to 1.
__outputB__ = m(x1B)

