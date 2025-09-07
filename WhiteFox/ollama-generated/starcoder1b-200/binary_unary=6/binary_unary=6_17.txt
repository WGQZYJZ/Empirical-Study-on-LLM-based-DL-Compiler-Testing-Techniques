
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 5 # Subtract 5 from the result of linear transformation
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()


