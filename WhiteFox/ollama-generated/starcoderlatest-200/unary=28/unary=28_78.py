
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32, 64)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.clamp_min(v1, min_value=0.)
        v3 = torch.clamp_max(v2, max_value=1.)
        return v3


# Initializing the model
m = Model()
m.set_args(
    min_value=torch.tensor(-1.),
    max_value=torch.tensor(1.)
)

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
