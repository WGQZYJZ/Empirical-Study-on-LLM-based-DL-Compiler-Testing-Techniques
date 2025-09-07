
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(256, 4)
        self.fc2 = torch.nn.Linear(4, 3)
 
    def forward(self, x):
        v = self.fc1(x)
        return self.fc2(v)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(3, 256)
y  = torch.randn(3, 4)
