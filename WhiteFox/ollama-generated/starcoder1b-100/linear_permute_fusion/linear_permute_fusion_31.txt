
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        v1 = torch.tanh(x1.permute(0, 2, 1))
        v2 = torch.sigmoid(torch.matmul(v1, self.linear.weight))
        return v2


# Initializing the model
m = Model()

