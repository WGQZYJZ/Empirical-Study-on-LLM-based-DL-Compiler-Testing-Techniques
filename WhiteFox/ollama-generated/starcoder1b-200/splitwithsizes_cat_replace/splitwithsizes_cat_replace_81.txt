
class Model(torch.nn.Module):
    def __init__(self, hidden_size, input_size, output_size):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(input_size, hidden_size, 1)
        self.pool = torch.nn.MaxPool2d(2, stride=2)
        self.fc   = torch.nn.Linear(hidden_size, output_size)
 
    def forward(self, x):
        v = self.conv1(x)
        v = self.pool(v)
        v = v.view(-1, self.in_features)
        v = F.relu(self.fc(v))
        return v


# Initializing the model
m = Model()


