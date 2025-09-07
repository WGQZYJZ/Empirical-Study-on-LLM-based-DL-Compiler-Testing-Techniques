
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2048, 1024)
        self.relu1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(1024, 1024)
        self.relu2 = torch.nn.ReLU()
        self.fc3 = torch.nn.Linear(1024, output_dim)
 
    def forward(self, x1):
        v1 = self.fc1(x1)  # [batch_size, sequence_len, feature_dim]
        v2 = self.relu1(v1)  # [batch_size, sequence_len, feature_dim]
        v3 = self.fc2(v2)  # [batch_size, sequence_len, feature_dim]
        v4 = self.relu2(v3)  # [batch_size, sequence_len, feature_dim]
        v5 = self.fc3(v4)  # [batch_size, sequence_len, output_dim]
        return v5

# Initializing the model
m = Model()

