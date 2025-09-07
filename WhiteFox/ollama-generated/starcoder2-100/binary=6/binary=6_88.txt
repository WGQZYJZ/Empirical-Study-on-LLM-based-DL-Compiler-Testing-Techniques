
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v2  = x1  # Just a fake output
        v4  = other - self.linear(v2)
        return v4


# Initializing the model