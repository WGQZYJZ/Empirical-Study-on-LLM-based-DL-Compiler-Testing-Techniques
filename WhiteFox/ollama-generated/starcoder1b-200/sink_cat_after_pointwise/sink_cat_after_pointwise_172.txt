
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)
        self.sinker = PointwiseUnarySinker()

    def forward(self, x1):
        v1 = x1.view(-1, 4).permute(0, 2, 1)
        v2 = torch.relu(v1)
        t1 = self.sinker(v2)
        return t1


# Initializing the model
config = configdict.ConfigDict()
m  = Model(config)
