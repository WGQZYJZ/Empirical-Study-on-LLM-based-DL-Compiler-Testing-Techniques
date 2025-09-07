
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1[:, 0:9223372036854775807] 
        v3 = v2[:, 0:size] 
        v4 = torch.cat([v1, v3], dim=1) 
        return v4

# Initializing the model