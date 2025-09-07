
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.fc1  = torch.nn.Linear(576, 400)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = v1 + 1  # Add 1 to the result of convolution
        v3  = torch.relu(self.fc1(v2))
        return v3


# Initializing the model
m = Model()

