
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(20, 15)
        self.fc2 = torch.nn.Linear(30, 1)
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1) # Create an input tensor with concatenated inputs from the first and second layers, respectively.
        v2 = self.fc1(v1) # Apply the first fully connected layer to this tensor
        v3 = self.fc2(v2) # Apply the last fully connected layer to this tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 10, requires_grad=True)
x2 = torch.randn(3, 256, requires_grad=True) # A random batch of inputs from a linear layer with 256 neurons.
