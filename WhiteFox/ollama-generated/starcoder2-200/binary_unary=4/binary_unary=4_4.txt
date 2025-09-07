
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Applying a linear transformation to the input tensor
        v2 = v1 + other  # Adding another constant tensor as the input of the ReLU activation function
        v3 = torch.relu(v2) # Applying a ReLU activation function to the output of the linear transformation and another constant tensors 
        return v3


# Initializing the model
m = Model()



# Inputs to the model
x1 = torch.randn(5, 32 * 32)
__output__  = m(x1)
other = torch.zeros_like(torch.randn(10))

