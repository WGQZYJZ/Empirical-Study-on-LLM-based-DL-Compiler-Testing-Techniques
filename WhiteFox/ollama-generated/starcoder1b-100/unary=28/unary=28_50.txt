
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        return torch.clamp_min(
            torch.clamp_max(self.linear(x1), min_value=0.), max_value=2.)


# Initializing the model
m = Model()
