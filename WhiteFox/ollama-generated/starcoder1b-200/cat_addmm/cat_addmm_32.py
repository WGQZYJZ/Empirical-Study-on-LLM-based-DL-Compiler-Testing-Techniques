
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(50, 20)
        self.fc2 = torch.nn.Linear(40, 20)
        self.fc3 = torch.nn.Linear(30, 10)
 
    def forward(self, x):
        v1 = torch.matmul(x, self.fc1.weight)
        v2 = torch.sigmoid(self.fc2(v1))
        v3 = torch.softmax(self.fc3(v2), dim=1)
        return v3


# Initializing the model
m  = Model()


