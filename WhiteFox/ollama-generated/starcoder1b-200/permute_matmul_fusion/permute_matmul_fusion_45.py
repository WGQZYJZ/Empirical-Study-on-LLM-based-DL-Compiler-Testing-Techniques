
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 4)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        v3 = torch.bmm(v1, v2)
        v4 = torch.matmul(v1, v2)
        return (
            self.linear1(x1),
            self.linear2(torch.cat((v3, v4), dim=-1)),
        )


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 4, 2)
