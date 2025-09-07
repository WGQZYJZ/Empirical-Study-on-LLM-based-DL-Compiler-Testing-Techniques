
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous()
        v2 = x2.permute(0, 2, 1).contiguous()

        mmm = torch.bmm(v1, v2)

        return mmm + self.linear(x1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2, 2)
x2 = torch.randn(2, 2, 2)
