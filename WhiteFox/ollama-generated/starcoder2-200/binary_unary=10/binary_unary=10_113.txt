
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25600 * 3, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor[0]
        v3  = F.relu(v2)
        return v3

# Initializing the model