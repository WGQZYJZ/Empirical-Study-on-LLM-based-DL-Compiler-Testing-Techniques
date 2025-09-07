
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1) # Add conv layer to model
        self.conv2 = torch.nn.Conv2d(8, 16, 1) # Add conv layer to model
 
    def forward(self, x):
        v0 = self.conv1(x) # Apply convolution on input tensor
        v1 = self.conv2(v0) # Apply another conv layer to the output of first conv layer
        return v1

# Initializing the model
m  = Model()

