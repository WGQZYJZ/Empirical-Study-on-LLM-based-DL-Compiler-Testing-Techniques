
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10000, 50)

    def forward(self, x):
        return self.linear(x).view(x.shape[0], -1)


# Initializing the model
m = Model()


