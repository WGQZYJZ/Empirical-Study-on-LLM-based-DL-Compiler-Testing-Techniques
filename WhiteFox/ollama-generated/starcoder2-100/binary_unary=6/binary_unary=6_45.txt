
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5, bias=True)
 
    def forward(self, x1):
        v2 = self.linear(x1) - 987654321 # Subtract 'other' from the output of the linear transformation
        v3 = torch.relu(v2) 
        return v3

# Initializing the model
m = Model()

