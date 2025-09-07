
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 256)
 
    def forward(self, x1):
        v1 = self.linear(x1) - other # Subtract 'other' from the output of the linear transformation
        v3 = torch.relu(v1) 
        return v3

# Initializing the model