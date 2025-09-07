
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*8*8, 1)
        self.other = ... # A tensor with the same shape as a linear transformation's output.
 
    def forward(self, x1):
        v0 = x1
        v1  = self.linear(v0)
        v2  = v1 + self.other
        v3  = torch.relu(v2)
        return v3

# Initializing the model