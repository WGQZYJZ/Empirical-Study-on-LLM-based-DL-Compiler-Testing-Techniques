
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15368974203618323):
        super().__init__()
        self.linear  = torch.nn.Linear(1024*5*5, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 > 0 # Create a boolean tensor where each element is True if the corresponding element in v1 is greater than 0, and False otherwise
        v3  = v1 * negative_slope # Multiply the output of the linear transformation by the negative slope
        v4  = torch.where(v2, v1, v3) # For each element in v2, if the element is True, choose the corresponding element from v1, otherwise choose the corresponding element from v3
        return v4

# Initializing the model
m = Model()

