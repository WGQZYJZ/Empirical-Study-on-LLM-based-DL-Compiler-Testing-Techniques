
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2,1)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = v1 + other # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()
other = torch.ones_like(v1) / m.__output__[0][0].item() # Generating a random tensor with the same size and shape as the tensor of the first linear transformation, divided by the absolute value of the first element in this tensor. This is to ensure that the first parameter of m.linear() is different from zero. The multiplication by m.__output__[0][0].item() makes it easier to get the first element out of a tensor with one element
m = Model(other=other) # Initialize the model with another tensor as its first linear transformation's bias


# Inputs to the model