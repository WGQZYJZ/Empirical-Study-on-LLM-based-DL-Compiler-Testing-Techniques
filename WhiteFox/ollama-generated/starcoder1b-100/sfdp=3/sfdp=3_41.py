
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(768, 512)
        self.fc2 = torch.nn.Linear(512, 512)
        self.fc3 = torch.nn.Linear(512, 256)
        self.fc4 = torch.nn.Linear(256, 256)
        self.fc5 = torch.nn.Linear(256, 768)
 
    def forward(self, x1):
        x1 = self.fc1(x1)
        x1 = self.dropout1(x1)
        x1 = F.relu(x1)
        x1 = self.fc2(x1)
        x1 = self.dropout2(x1)
        x1 = F.relu(x1)
        x1 = self.fc3(x1)
        x1 = self.dropout3(x1)
        x1 = F.relu(x1)
        x1 = self.fc4(x1)
        x1 = self.dropout4(x1)
        x1 = F.relu(x1)
        x1 = self.fc5(x1)
        return x1


# Initializing the model
m = Model()


