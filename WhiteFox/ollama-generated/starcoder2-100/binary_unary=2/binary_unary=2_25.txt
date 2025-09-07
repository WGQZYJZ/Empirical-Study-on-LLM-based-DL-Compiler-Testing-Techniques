
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other # Subtract a tensor or scalar "other" from the output of the convolution
        v3  = torch.relu(v2) 
        return v3


# Initializing the model
m  = Model()
 

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 

# Saving the initial state of the weights in the model
state_dict  = m.conv.weight
 
 

# Generating a tensor with random values for "other"
other  = torch.randn((3, 3, 1, 2))

 # Calculating the output produced by applying pointwise convolution to the input x1 
 __output__  = m(x1)
 
