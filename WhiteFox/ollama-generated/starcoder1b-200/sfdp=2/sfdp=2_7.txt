
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1  = torch.nn.Linear(8 * (window_size // 2), hidden_size)
        self.dropout = torch.nn.Dropout(0.25)
        self.fc2 = torch.nn.Linear(hidden_size, 10)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v1 = self.dropout(F.relu(v1))
        x2 = v1.view(-1, 8 * (window_size // 2), 1, 1)
        output = F.relu(self.fc1(x2)).view(-1, hidden_size)
        return self.fc2(output)


# Initializing the model
m = Model()

