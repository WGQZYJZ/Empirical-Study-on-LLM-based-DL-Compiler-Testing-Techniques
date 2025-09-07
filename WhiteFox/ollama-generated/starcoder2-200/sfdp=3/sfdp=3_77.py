
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.relu   = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(4, 6)
 
    def forward(self, x):
        v0 = self.linear1(x)
        v1 = v0 + 0.5
        v2 = self.relu(v1)
        v3 = v2 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4  + 1 
        v6 = v1 * v5
        v7 = self.linear2(v6)
        return v7


# Initializing the model
m = Model()

# Input to the model: 
x_0 = torch.randn(3, 4)

# Output of the model for the input above is: 