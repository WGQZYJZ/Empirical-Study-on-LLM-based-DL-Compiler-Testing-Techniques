
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other
        return v2


# Initializing the model with initial values of 'other' set to zero:
m = Model()
m.__parameters__[0].data[:] = torch.randn_like(m.__parameters__[0]) # randomly initialize the parameters for linear layer (torch.nn.Linear in our example)
m.__parameters__[1].data[:]= 0
other = m.__parameters__[1]


# Inputs to the model: 
x1 = torch.randn(32, 10) # random input tensor of size batch_size x embedding dimensionality

# Call forward function in pytorch
