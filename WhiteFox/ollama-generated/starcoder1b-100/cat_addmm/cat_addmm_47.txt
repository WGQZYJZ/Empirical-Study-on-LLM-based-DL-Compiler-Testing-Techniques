
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 64)
        self.fc2 = torch.nn.Linear(64, 64)
 
    def forward(self, x):
        h  = F.relu(self.fc1(x))
        h  = F.relu(self.fc2(h))
        y1 = torch.mean(h, dim=1)
        y2 = self.fc2(y1).reshape(-1, 1) # Reshape the output of fc2 to get a tensor of size batch_size * input_size
        return y2


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(3, 64)
