
class Model(torch.nn.Module):
    def __init__(self, other=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(32, 32)
        self.relu   = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.addmm(other, x, x)
        return self.relu(v2)


# Initializing the model
m  = Model()


