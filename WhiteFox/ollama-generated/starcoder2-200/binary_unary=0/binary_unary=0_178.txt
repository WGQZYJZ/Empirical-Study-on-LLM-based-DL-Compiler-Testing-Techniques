
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply a convolution to the input tensor
        v2  = v1 + other_tensor
        v3  = F.relu(v2)    # Apply a ReLU activation function to the result
        return v3

m  = Model()

# Input tensors for the model
x1  = torch.randn(1, 3, 64, 64)
other_tensor = other_value * torch.ones_like(x1) # Create another tensor of same size with random values in [0; 1]

