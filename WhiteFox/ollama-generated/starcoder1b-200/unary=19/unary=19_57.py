
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28, 1)

    def forward(self, x):
        x = self.linear(x).view(x.size()[0], -1)
        return F.sigmoid(x)


# Initializing the model
m = Model()


