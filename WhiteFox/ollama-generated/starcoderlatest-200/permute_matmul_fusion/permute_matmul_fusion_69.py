
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 3)
        self.linear_B = torch.nn.Linear(3, 4)

    def forward(self, x1):
        v1 = torch.bmm(x1, x1)
        v2 = x1.permute(0, 2, 1)
        v3 = torch.matmul(v2, self.linear_A.weight)

        # Output: [batch, n, h] where n is the number of hidden units in linear layer 1
        v4 = torch.bmm(x1, self.linear_B.weight)

        return v1 + v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 2, 2)
