
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 6)
        self.fc2 = torch.nn.Linear(6, 4)
 
    def forward(self, x):
        return self.fc2(self.fc1(x))


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 3)
