
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 1)
        return t2 + self.relu(t2).expand_as(t2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 4, 3)
x2 = torch.randn(2, 5, 3)
