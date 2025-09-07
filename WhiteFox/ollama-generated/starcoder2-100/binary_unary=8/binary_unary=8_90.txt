
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + other # Replace with a valid input tensor. You can call `torch.randn(...)` to generate a new valid input for the model. 
        v3  = torch.relu(v2)
        return v3

# Initializing the model and setting up the random seed
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # The model should accept random inputs of shape (1, 3, 64, 64). You can call `torch.randn(...)` to generate a new valid input for the model. 
other = torch.tensor([0.5] * 28*28*8)


# Initializing the model and setting up the random seed
m  = Model()

# Inputs to the model