
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 > 0 # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        slope = torch.full((v1), 0.5)
        v3   = v1 * slope # Multiply the output of the linear transformation by the negative slope
        result = torch.where(v2, v1, v3) 
        return result


# Initializing the model