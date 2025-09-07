
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # Use kernel size 1 to generate a new input tensor
        self.fc1   = torch.nn.Linear(8 * 64 * 64, 10)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.view(v1.shape[0], -1).float() # Recover the shape of the original input tensor (i.e. it can be broadcasted to any number of dimensions)
        v3 = torch.nn.functional.relu(self.fc1(v2))
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
