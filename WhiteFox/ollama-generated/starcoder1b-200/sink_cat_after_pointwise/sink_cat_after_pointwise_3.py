
class Model(torch.nn.Module):
    def __init__(self, in_features: int, hidden: int, out_features: int):
        super().__init__()
        self.fc1 = torch.nn.Linear(in_features, hidden)
        self.relu = nn.ReLU()
        self.dropout1 = nn.Dropout(p=0.5)
        self.fc2 = torch.nn.Linear(hidden, out_features)

    def forward(self, x):
        h = self.fc1(x)
        h = self.relu(h)
        h = self.dropout1(h)
        o = self.fc2(h)
        return o


# Initializing the model
m  = Model()
input_tensor = torch.randn(1, in_features=in_features, hidden=hidden, out_features=out_features)
