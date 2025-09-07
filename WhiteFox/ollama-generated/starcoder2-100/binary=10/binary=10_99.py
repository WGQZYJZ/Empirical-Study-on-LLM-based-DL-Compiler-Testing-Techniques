
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v2 = other
        v1 = self.linear(x1)
        v3  = v1 + v2 
        return v3

# Initializing the model