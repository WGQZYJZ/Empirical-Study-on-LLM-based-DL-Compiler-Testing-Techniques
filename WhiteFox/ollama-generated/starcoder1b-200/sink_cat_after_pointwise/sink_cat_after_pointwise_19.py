
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous()
        v2 = torch.relu(x2.contiguous().view(x2.size(0), -1))
        return self.linear(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(3, 3, 3)
