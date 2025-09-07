
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0 # Apply the linear transformation to the input tensor
        v2 = v1 * negative_slope # Multiply the output of the linear transformation by the negative slope
        v4 = torch.where(v1 > 0, x1, v2) # For each element in t1, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
