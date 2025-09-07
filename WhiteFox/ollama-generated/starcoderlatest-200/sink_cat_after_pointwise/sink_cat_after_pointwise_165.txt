
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = v1.view(-1, v1.shape[1] * v1.shape[2])
        return torch.nn.functional.relu(torch.matmul(v2, self.linear.weight), self.linear.bias)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 2, 10)
x2 = torch.randn(8, 3,  20)
