
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 > 0).float() # For each element in the input tensor v1: If the corresponding element is greater than or equal to zero then it should return a floating point value of one; otherwise return a floating point value of zero 
        v3 = -negative_slope * v2 + self.linear(x)
        v4 = torch.where(v2, x, v3) # If the boolean tensor contains True for each element in v1 then return corresponding element from the input tensor; otherwise choose correponding elements from the output of multiplication by a negative slope 
        return v4


# Initializing the model
m = Model()


# Inputs to the model 
x = torch.randn(2, 10) # Input tensor with size (2, 10)
