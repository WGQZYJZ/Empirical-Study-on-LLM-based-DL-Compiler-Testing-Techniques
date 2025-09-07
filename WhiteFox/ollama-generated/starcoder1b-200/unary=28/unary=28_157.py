
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, min_value=0, max_value=127):
        v1 = self.linear(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Initializing the model
m = Model()
__output__  = m(x1)
