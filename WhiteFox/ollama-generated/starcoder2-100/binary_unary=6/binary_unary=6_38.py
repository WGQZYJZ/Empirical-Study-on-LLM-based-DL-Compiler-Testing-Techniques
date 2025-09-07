
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # <-- 'other' is the constant to subtract 
        v3 = torch.relu(v2) # Apply the ReLU activation function 
        return v3
# Initializing the model