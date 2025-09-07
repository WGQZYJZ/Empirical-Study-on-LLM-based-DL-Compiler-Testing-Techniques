

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other = 0.5
    
    def forward(self, x1):
        v1 = self.linear(x1) + self.other # line 24
        return v1

# Initializing the model