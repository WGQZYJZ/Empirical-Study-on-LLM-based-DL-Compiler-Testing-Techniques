
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(5041, 32)
    
    def forward(self, x):
        v1  = self.linear(x) 
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model