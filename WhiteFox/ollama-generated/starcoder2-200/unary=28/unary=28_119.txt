
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
        self.linear  = torch.nn.Linear(32*32*8,10)
        self.min = min_
        self.max = max_

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, self.min)
        v3  = torch.clamp_max(v2, self.max)

        return v3
# Initializing the model
m  = Model(0., -9.)


# Inputs to the model