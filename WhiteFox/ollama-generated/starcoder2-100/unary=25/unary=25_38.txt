
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.conv(x1) #Apply a linear transformation to the input tensor
        v2  = v1 > 0    # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise 
        v3  = -v2*v2 # Multiply the output of the linear transformation by the negative slope. For each element in v2 that is True, multiply the corresponding element from v1 by -1; for each element in v2 that is False, leave the corresponding element unchanged
        v4  = torch.where(v2, v1, v3) #For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3)
__output__  = m(x1)