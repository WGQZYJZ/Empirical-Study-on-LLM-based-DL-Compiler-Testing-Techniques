
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64*8, 1024)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        # Apply a linear transformation to the input tensor
        v1 = self.linear(x)
        # Add another tensor to the output of the linear transformation
        v2 = v1 + 5
        # Apply the ReLU activation function to the result
        v3 = self.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
