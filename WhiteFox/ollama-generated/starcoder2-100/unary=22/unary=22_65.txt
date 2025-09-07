
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1) # tanh() is the same as nn.Tanh()
        return v2

# Initializing the model