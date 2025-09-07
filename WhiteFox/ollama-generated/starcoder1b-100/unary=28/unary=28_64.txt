
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)

    def forward(self, x1, *min_max):
        return self.linear(x1) * min_max


# Initializing the model
m = Model()


