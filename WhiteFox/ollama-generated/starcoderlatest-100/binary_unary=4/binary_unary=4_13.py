
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_tensor = torch.randn(64*64, dtype=torch.float32, requires_grad=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other_tensor # Add another tensor to the output of the linear transformation
        v3 = torch.nn.functional.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
