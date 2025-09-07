
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 8)

    def forward(self, x1, x2):
        return self.linear(x2) + x1


# Initializing the model
m = Model()


