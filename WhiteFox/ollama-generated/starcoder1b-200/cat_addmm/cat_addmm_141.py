
class Model(torch.nn.Module):
    def __init__(self, n_features, n_classes):
        super().__init__()
        self.fc1 = torch.nn.Linear(n_features, 32)
        self.fc2 = torch.nn.Linear(32, 32)
        self.fc3 = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        x  = self.fc1(x)
        x = F.relu(x)
        x  = self.fc2(x)
        x  = F.relu(x)
        x  = self.fc3(x)
        return x


# Initializing the model
m = Model(32, 10)


# Inputs to the model
x1 = torch.randn(1, 32)
x2 = torch.randn(1, 32)
