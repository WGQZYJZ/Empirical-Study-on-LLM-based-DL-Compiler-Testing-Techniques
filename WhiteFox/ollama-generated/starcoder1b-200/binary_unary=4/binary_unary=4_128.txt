
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x, other=None):
        v1 = self.linear(x) + other # Add another tensor to the output of the linear transformation
        v2 = relu(v1) # Apply the ReLU activation function to the result
        return v2


# Initializing the model
m  = Model()


# Inputs and parameters
input_tensor  = torch.randn(10, 3) 
params         = input_tensor * 2 # A tensor containing a tensor of numbers representing two numbers in a linear combination
__output__  = m(input_tensor, params=params)

