
class Model(torch.nn.Module):
    def __init__(self, negSlope=0.5):
        super().__init__()
        self.linear = torch.nn.Linear(784, 1)
        self.negSlope = negSlope
 
    def forward(self, x):
        v1 = self.linear(x) # Apply a linear transformation to the input tensor
        v2 = (v1 > 0).float() # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v3 = v1 * self.negSlope # Multiply the output of the linear transformation by the negative slope
        v4 = torch.where(v2 == v1, v3) # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return v4

# Initializing the model
m  = Model(0.5)

 # Inputs to the model
x = torch.rand(784).reshape(1,-1)
