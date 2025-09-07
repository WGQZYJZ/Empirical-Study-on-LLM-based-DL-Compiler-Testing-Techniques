
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x1, min_value=50, max_value=20):
        y1 = self.linear(x1)
        y2 = torch.clamp_min(y1, min_value)
        y3 = torch.clamp_max(y2, max_value)
        return y3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 10)
