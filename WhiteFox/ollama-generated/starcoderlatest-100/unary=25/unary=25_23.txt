
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() # create a boolean tensor where each element is True if the corresponding element in v1 is greater than 0, and False otherwise
        v3 = v1 * -1.5e-4 # multiply the output of the linear transformation by the negative slope
        v4 = torch.where(v2, v1, v3) # for each element in the boolean tensor, if the corresponding element in v2 is True, choose the corresponding element from the output of the linear transformation, otherwise choose the corresponding element from v3
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
