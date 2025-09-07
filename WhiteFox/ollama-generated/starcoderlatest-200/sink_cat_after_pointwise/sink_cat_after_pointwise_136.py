
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu1 = torch.nn.ReLU()

    def forward(self, x):
        t1 = torch.cat([x, 2 * x], dim=0)
        t2 = t1.view(-1, 2)
        t3 = self.relu1(t2)
        return t3

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3)
