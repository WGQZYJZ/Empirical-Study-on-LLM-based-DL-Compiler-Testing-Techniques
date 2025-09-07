
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[1, 3]):
        super().__init__()
        self.split = torch.split
        self.cat   = torch.cat

    def forward(self, x1):
        return self.split(x1, self.split_sizes)

# Initializing the model
m = Model()


