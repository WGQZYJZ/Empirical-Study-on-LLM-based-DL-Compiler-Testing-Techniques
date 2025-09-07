
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28 + 30, 1)
 
    def forward(self, x1):
        v1 = F.relu(x1[:, 75:].sum(dim=1).reshape(-1))
        v4 = self.linear(v1)
        return torch.sigmoid(v4), F.softmax(v4, dim=-2)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(10, 385 + 70 + 95)


