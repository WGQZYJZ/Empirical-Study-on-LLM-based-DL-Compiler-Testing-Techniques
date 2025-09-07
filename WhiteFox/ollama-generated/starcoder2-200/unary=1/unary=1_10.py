
m = nn.Linear(784, 50)
 
# Initializing the model
m1 = nn.Sequential() # Create a sequential container for the first block
m2 = nn.Sequential() # Create a sequential container for the second block

# Inputs to the model and containers
i = torch.randn(32, 784)
 
# First block (taking input i into m1):
m1.add_module("linear", nn.Linear(784, 50)) # Add linear transformation as a module in container with name "linear"
m1.add_module("relu", nn.ReLU()) # Add ReLU non-linearity to the container
__output1 = m1(i)
 
# Second block (taking input t2 from m1 into m2):
m2.add_module("conv", nn.Conv2d(50, 8, 3)) # Add a convolutional layer to the second block with 50 input channels and 8 output channels with kernel size 3
m2.add_module("relu", nn.ReLU()) # Add ReLU non-linearity to the container
__output2 = m2(m1)

