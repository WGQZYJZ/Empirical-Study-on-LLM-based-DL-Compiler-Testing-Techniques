
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25088, 147)
 
    def forward(self, x):
        v1  = self.linear(x) # Apply linear transformation to the input tensor
        v2  = v1 + other      # Add another tensor to the output of the linear transformation
        v3  = torch.nn.functional.relu(v2) # Apply ReLU activation function to the result
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1   = torch.randn(50, 64*64*8).view(-1, 64*64*8) # Create a 2D tensor of shape (50 x 25088), where each row is a linear combination of the features in an image.
other = torch.randn(50, 64*64*8).view(-1, 64*64*8) # Create a 2D tensor of shape (50 x 25088), where each row is a linear combination of the features in another image.
