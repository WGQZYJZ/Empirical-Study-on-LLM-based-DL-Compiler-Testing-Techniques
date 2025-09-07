
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 4, 6000)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor. In this example, a constant of -1 will be added. 
        v2 = v1 - (-1.)
        v3 = torch.relu(v2) # Apply ReLU activation function to the result of subtracting 'other' from the output of the linear transformation. 
        return  v3


# Initializing model