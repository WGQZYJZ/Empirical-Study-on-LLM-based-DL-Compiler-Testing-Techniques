
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 32)
        self.other = other
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return (v1 - self.other).clamp_min_(0.)


# Initializing the model
m = Model(-2)
