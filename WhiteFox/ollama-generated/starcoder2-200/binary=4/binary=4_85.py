
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Initialize the layer with weight and bias tensors for the pattern
        self.linear = torch.nn.Linear(50, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 + other_tensor
        return v3

# Initializing the model with a weight and bias tensor
w1  =  torch.randn(8*8*50) # initialize the weight as the output size of the first convolutional layer
b1 = torch.randn(2)  # Initialize the bias to be the output dimension of the second layer.
self.linear  = self.nn.Linear(8*8*50, 2).cuda()
self.linear.weight  = w1
self.linear.bias  = b1


# Initializing a second model with different weight and bias tensor from the previous one

# Model
class Model_two(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Initialize the layer with weight and bias tensors for the pattern
        self.linear = torch.nn.Linear(50, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 + other_tensor
        return v3

# Initializing a second model with different weight and bias tensor from the previous one
w2  =  torch.randn(8*8*50)# initialize the weight as the output size of the first convolutional layer in the second model
b2 = torch.randn(1) # Initialize the bias to be the output dimension of the second layer.
self.linear  = self.nn.Linear(8*8*50, 1).cuda()
self.linear.weight  = w2
self.linear.bias  = b2


# Inputs to both models
x2 = torch.randn(3, 8, 8) # the input tensor from the first model
x3 = torch.randn(4, 50, 1, 1)# the input tensor for the second model



