
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 3)

    def forward(self, x1): 
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + 3 # Add 3 to the output of the linear transformation
        v3 = F.relu6(v2) # Clamp the output of the addition operation to a minimum of 0 and a maximum of 6
        v4 = torch.div(v3, 6) # Divide the output of the previous operation by 6
        return v4

# Initializing the model
m1 = Model()


# Inputs to the model
x1 = torch.randn(2000, 857) # Generate random input tensor with size [batch_size x num_channels] for model m
x2 = torch.randn(43655)

# Initializing the model with input tensor 1
m1(x1)


# Initializing the model with input tensor 2, this will fail as it violates the requirement
m1(x2)


