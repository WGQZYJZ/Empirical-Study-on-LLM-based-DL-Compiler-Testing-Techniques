
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)

    def forward(self, x):
        return self.linear(x.permute(0, 2, 1))


# Initializing the model
m = Model()


