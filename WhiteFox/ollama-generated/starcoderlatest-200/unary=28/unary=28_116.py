
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1, min_value=None, max_value=None):
        v1 = self.linear(x1)
        if min_value is None:
            v2 = torch.clamp(v1, min=0)
        else:
            v2 = torch.clamp(v1, min=min_value)
        if max_value is None:
            v3 = torch.clamp(v2, max=None)
        else:
            v3 = torch.clamp(v2, max=max_value)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, 10)
