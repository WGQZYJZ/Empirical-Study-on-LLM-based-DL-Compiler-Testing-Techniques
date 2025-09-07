
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 64 * 8, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other_tensor 
        v3  = torch.relu(v2)
        return v3


# Initializing the model