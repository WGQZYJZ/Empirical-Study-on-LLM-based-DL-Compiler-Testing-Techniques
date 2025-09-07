
class Model(torch.nn.Module):
    def __init__(self, hidden_size, output_size, concat_dimension=1):
        super().__init__()
 
        self.fc1 = torch.nn.Linear(hidden_size * 2, hidden_size)
        self.relu1 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, output_size)
 
    def forward(self, x1, x2):
        x3  = torch.cat([x1, x2], dim=concat_dimension)
        v1  = self.relu1(self.fc1(x3))
        v2  = self.fc2(v1)
        return v2


# Initializing the model
m = Model(hidden_size=3, output_size=5, concat_dimension=1)


