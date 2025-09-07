
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3*64*64, 80)
        self.relu1 = torch.nn.ReLU()
 
    def forward(self, x2):
        v1 = self.relu1(self.fc1(x2))
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn(1, 3*64*64)
