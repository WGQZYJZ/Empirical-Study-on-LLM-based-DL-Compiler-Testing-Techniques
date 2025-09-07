
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64, 32)
        self.linear2 = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v0  = self.linear1(x1) # Apply the first linear transformation to input tensor (x1).
        v1 = v0 + other  # Add another tensor (other) to output of linear transformation
        v2 = self.linear2(v1) # Apply second linear transformation on result of the first linear transformation. 
        return v2

# Initializing model, with a custom parameter value for `other`
m = Model()
other  = torch.tensor([[[[-0.5]]]])

# Inputs to the model
x1  = torch.randn(1, 64)

__output__  = m(x1)

