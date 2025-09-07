
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 4)
        t3 = self.relu(t2)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 8, dtype=torch.float32)
x2 = torch.randn(16, 4, dtype=torch.float32)
