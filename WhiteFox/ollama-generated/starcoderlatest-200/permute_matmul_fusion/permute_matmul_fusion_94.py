
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)

        if __random_function__:
            v1, v2 = torch.rand(x1.shape), torch.rand(x2.shape)

        return torch.matmul(v1, v2) + self.linear(torch.cat((x1, x2), dim=-1))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 3, 2)
