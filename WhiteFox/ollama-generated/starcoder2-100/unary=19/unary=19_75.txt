
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation
        return v2

# Initializing the model
m = Model()

