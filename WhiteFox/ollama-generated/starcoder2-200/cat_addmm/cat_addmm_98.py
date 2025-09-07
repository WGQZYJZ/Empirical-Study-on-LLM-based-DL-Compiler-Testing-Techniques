

class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        
        self.dim = dim

        self.lin1  = torch.nn.Linear(784, 50)
        self.lin2  = torch.nn.Linear(50, 30)
 
    def forward(self, x):
    
        y1  = self.lin1(x)
        y2  = self.lin2(y1)

        y2  = y2 + y1 # The output of the previous linear layer is added to the output of the current linear layer
        y3  = torch.nn.functional.relu(torch.cat([y2], dim=self.dim)) # Concatenate the result along a specified dimension
        
        return y3


# Initializing the model
m  = Model(0)


# Inputs to the model
input_tensor1  = torch.randn(4, 784)  # A randomly generated 2D tensor of size 4 x 784
input_tensor2  = input_tensor1 * 5  # Multiply an array by a constant and convert it into another 2D tensor


__output__  = m(input_tensor2)

[Back to overview](README.md)
