
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 8)
 
    def forward(self, x):
        v1 = self.linear(x) - 30.5
        v2 = relu(v1)
        return v2

# Initializing the model
m = Model()

