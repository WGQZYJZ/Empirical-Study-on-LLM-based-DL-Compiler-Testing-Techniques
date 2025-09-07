
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying a linear transformation to the input tensor
        v2  = v1 > 0  # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        negative_slope  = -3
        v3  = v1 * negative_slope  # Multiplying the output of the linear transformation by a negative slope.
        v4  = torch.where(v2 , v1, v3)  # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return v4
 
# Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(80, 8)

 