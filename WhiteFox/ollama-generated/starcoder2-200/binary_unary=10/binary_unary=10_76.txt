
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3276800, 1)
 
    def forward(self, x):
        v1 = self.linear(x) 
        v2 = v1 + 50 * x # Some other tensor
        v3 = F.relu(v2)
        return v3

# Initializing the model
m = Model()

