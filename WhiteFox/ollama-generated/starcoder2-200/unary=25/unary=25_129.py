
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 64, 32)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applies a linear transformation to the input tensor.
        v2  = (v1 > 0).type_as(v1) # Creates a boolean tensor where each element is True if its corresponding element in the output of applying a linear transformation is greater than zero, and False otherwise.
        v3  = torch.where(v2, v1, -v1 * negative_slope) # For each element in the boolean tensor created above, if that element is True, choose the corresponding element from t1; otherwise choose the corresponding element from multiplying by negative slope. This essentially implements the Leaky ReLU activation function.
        return v3

# Initializing the model 
m = Model()
negative_slope = -0.25

 # Inputs to the model 
 x1  = torch.randn(1, 64 * 64)

 