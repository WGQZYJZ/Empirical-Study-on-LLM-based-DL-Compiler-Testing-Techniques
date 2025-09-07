
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(28*28, 5)(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other_tensor() 
        v3  = torch.nn.functional.relu(v2)   # Apply the ReLU activation function to the result of the linear transformation and add another tensor to it
        return v3


# Initializing the model
m  = Model()
other_tensor = torch.randn([10]) # Passing in a tensor as an argument


# Inputs to the model
x1  = torch.randn(5, 28*28)
 
# Initializing a dummy tensor for the other function call
other_tensor  = torch.randn([])
 
__output__  = m(x1)

