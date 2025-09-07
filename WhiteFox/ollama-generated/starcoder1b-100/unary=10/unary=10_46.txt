
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.relu1  = torch.nn.ReLU()
        self.relu2  = torch.nn.ReLU()

    def forward(self, x):
        l1   = self.linear1(x)
        l2   = l1  + 3
        l3   = torch.clamp_min(l2, 0)
        l4   = torch.clamp_max(l3, 6)
        l5   = l4 / 6
        return self.relu1(l5)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
