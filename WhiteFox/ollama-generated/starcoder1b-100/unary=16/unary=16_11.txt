
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 8)
        self.fc2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = relu(v1)
        v3 = self.fc2(v2)
        return v3


# Initializing the model
m = Model()


