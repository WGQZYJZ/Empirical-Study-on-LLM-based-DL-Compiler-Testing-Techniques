
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3072, 4096)
        self.fc2 = torch.nn.Linear(4096, 512)
 
    def forward(self, x1):
        v1 = self.fc1(x1) # Fully connected layer with the size of input (3072) and the size of output (4096)
        v2 = torch.relu(v1) # Apply ReLU to the output of the fully-connected layer
        v3 = self.fc2(v2) # Fully connected layer with the size of input (4096) and the size of output (512)
        return torch.cat([v3], 0)
 
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 3072)
