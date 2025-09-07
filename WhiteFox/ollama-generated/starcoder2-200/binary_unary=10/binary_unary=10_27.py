
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 + other
        v3 = torch.relu(v2) # Add another tensor to the output of the linear transformation, and finally the ReLU activation function is applied to the result.
        return v3


# Initializing the model
m  = Model()
 
x1  = torch.randn(100, 10) # Creating a 2-D matrix as an input tensor that meets the shape requirement in the linear transformation layer.
other  = torch.ones((100,5)) # Creating another random 2-D tensor of the same shape as the output of the linear transformation and the input tensor. The other tensor is used to add to v3.

__output__  = m(x1)
