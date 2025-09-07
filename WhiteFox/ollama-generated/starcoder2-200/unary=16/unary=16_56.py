
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4 * 64 + 1, 25)

    def forward(self, x1):
        t1 = self.linear(x1)
        v2 = torch.relu(t1) #  ReLU
        return v2


# Initializing the model
m = Model()
