
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024 * 8, 75)
        self.other  = torch.randn(33).view(-1, 33)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2  = v1 + self.other 
        v3  = torch.relu(v2)
        return v3


# Initializing the model