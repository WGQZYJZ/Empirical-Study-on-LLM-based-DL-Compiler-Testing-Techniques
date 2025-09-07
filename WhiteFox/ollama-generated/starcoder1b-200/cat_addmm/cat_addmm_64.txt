
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc = torch.nn.Linear(8, 5)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 + 1 # Add 1 to the output of conv1
        v3 = self.fc(v2) # Perform a linear operation on the output of conv1, and then concatenate along dim 1
        return v3


# Initializing the model
m = Model()

