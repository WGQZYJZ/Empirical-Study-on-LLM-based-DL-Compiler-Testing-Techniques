
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 3)
        self.linear_2 = torch.nn.Linear(3, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = x2.permute(0, 2, 1)

        v1 = torch.bmm(t1, self.linear_1.weight) + self.linear_1.bias # or torch.matmul(t1, self.linear_1.weight) + self.linear_1.bias
        v2 = torch.matmul(v1, self.linear_2.weight) + self.linear_2.bias

        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 2, 4)
