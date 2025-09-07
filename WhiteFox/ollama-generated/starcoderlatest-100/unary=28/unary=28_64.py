
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=self.args.vmin1)
        v3 = torch.clamp_max(v2, max_value=self.args.vmax1)
        return v3


# Initializing the model
m = Model()
m.args = Arguments('--vmin1 0 --vmax1 1')

# Inputs to the model
x1 = torch.randn(1, 10)
