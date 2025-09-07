
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3,4)
 
    def forward(self, x1): 
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the linear transformation.
        return v2
# Initializing model
m  = Model()

# Inputs to the model
x1 = torch.randn(3,4)
__output__  = m(x1)

# Expected outputs after forward propagation for the model in __model_definition__.
# If there are multiple possible outputs of the forward propagation, please pick one with a reasonable shape and data type.
__expected_outputs__ = [
  torch.tensor([[-0.,   -3.2791],
  [-4.5846e-04,  -0.       ],
  [ 0.0296,   3.2023]])]

# Please make sure that there is no output difference by a very small value.
# The precision should not be smaller than 1e-7 for each value in the output tensors.

