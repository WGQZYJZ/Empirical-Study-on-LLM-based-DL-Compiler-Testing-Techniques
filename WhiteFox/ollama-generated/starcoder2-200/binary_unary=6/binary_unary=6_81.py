
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
        self.other = 10
        
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - self.other
        v3 = F.relu(v2)
        return v3

# Initializing the model