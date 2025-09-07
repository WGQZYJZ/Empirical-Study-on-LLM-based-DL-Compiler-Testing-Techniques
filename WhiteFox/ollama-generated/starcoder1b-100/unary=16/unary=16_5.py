
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(200, 256)
        self.fc2 = torch.nn.Linear(256, 100)
        self.fc3 = torch.nn.Linear(100, 1)
 
    def forward(self, x):
        v1  = self.fc1(x)
        v2 = relu(v1)
        v3 = self.fc2(v2)
        v4 = relu(v3)
        v5 = self.fc3(v4)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 200)
