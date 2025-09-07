
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(20, 1)
 
    def forward(self, x1, y):
        v1  = self.linear(x1)
        v2  = v1 + y
        v3  = torch.relu(v2)
        return v3


# Initializing the model