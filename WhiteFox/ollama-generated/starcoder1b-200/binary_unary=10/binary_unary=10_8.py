
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 32, 10)
 
    def forward(self, x1, x2=None):
        v1 = x1.view(-1, 64, 32)
        v2 = self.linear(v1).view(-1, 10)
        if x2 is not None:
            v3 = x2 + v2
        else:
            v3 = v2
        return torch.relu(v3)


# Initializing the model
m = Model()
x1 = torch.randn(1, 64 * 32)
