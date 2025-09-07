
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_features=3, out_features=4)
        self.fc2 = torch.nn.Linear(in_features=4, out_features=3)
 
    def forward(self, x1):
        x2 = self.fc1(x1)
        x3 = self.fc2(x2)
        return x3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 3)
