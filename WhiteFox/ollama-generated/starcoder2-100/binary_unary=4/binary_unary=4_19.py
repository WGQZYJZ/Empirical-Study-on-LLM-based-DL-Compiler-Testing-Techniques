
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v2 = x1
        v3  = self.linear(v2)
        v4 = v3 + other_tensor # Replace the value of `other` by a random value.
        v5 = torch.relu(v4)
        return v5

# Initializing the model
m = Model()

