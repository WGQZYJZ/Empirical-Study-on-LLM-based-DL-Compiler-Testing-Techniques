
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(d_model, d_model)
        self.drop = nn.Dropout()
        self.fc2 = torch.nn.Linear(d_model, 300)
        self.fc3 = torch.nn.Linear(300, 256)
        self.out = torch.nn.Linear(256, num_classes)
 
    def forward(self, x1, x2):
        v1 = self.drop(F.relu(self.fc1(x1)))
        v2 = self.drop(F.relu(self.fc2(v1)))
        v3 = F.log_softmax(self.fc3(v2), dim=-1)
        return torch.mean(v3, dim=-1)


# Initializing the model
m  = Model()


