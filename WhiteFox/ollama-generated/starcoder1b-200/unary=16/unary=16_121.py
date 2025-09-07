
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 4)
        self.fc2 = torch.nn.Linear(4, 3)
 
    def forward(self, x1):
        t1 = self.fc1(x1)
        t2 = relu(t1)
        return self.fc2(t2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
