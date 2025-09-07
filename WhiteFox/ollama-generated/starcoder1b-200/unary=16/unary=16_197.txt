
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(64*64, 64)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(x1.shape[0], -1) # Flatten the input tensor into a vector
        v2 = self.linear(v1)                 # Apply the linear transformation to the flattened tensor
        return torch.nn.functional.relu(v2)


# Initializing the model
m = Model()


