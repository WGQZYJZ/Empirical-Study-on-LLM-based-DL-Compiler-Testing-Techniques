
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2, x3):
        v1 = torch.cat([x1, y2], dim=0) # Concatenate 2 tensors along the first axis (dimension 0). 
        v2 = v1.view(-1, )  # Reshape the concatenated tensor to a 1-dimensional vector
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(2, 50) # A random 2D tensor of shape [2 x 50] for input 1
y2 = torch.randn(784, 3932) # A 2D random tensor with shape  [784 x 3932] for input 2
x3 = torch.randn(3932, ) # A vector of size 3932 as an input to the model

