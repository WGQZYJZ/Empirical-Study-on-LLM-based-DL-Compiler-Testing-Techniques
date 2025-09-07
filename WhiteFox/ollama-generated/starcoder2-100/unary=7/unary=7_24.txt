
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = clamp(min=0, max=6, l1 + 3) # where l1 is the output of a linear transformation in this model
        v3  = v2 * v1
        return v3 / 6


# Initializing the model