

class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.25):
        super().__init__()
        self.linear = torch.nn.Linear(16384, 4096)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = (v1 > 0).float() # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise 
        v3 = negative_slope * v1 * ((-v1 + -2.8937645) < 0).float()
        v4 = torch.where(v2, v1, v3) # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3 
        return v4

# Initializing the model
m  = Model(-0.5)

