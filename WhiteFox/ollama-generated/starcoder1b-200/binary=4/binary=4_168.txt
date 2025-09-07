
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)

    def forward(self, x1):
        return self.linear1(x1) + other


# Initializing the model
m = Model()

