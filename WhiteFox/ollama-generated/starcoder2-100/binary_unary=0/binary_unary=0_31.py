
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = other_tensor + v1  # This tensor was created in a previous iteration of the model
        v5  = torch.relu(v4)  # Apply the ReLU activation function to the result
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
x1   = torch.randn(1, 3, 64, 64)
other_tensor = x1 + 5 # this tensor was created in a previous iteration of the model 
