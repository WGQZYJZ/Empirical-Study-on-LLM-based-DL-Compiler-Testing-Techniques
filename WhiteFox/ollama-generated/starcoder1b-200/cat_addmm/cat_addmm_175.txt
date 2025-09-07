
class Model(torch.nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()
        self.fc1 = torch.nn.Linear(3 * 64 * 64, 200)
        self.relu = torch.nn.ReLU()
        self.drop = torch.nn.Dropout(0.7)
        self.fc2 = torch.nn.Linear(200, num_classes)
 
    def forward(self, x):
        v = x.view(x.size()[0], -1)  # Flatten the input into a vector
        v = self.relu(self.drop(self.fc1(v)))  # Apply ReLU and dropout to the result of linear layer 1
        v = self.relu(self.drop(self.fc2(v)))  # Apply ReLU and dropout to the result of linear layer 2
        return v


# Initializing the model
m = Model()


