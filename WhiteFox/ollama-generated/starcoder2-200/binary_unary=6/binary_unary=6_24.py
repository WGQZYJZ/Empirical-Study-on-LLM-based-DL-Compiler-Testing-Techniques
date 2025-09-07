
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_const
        v3 = torch.relu(v2) # Applying ReLU
        return v3


# Initializing the model