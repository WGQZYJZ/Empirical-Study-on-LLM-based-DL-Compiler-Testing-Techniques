
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v2 = torch.Tensor([3, 4]) # Initialize another tensor with [3, 4] as its elements
 
        v5  = self._linear_transformation(x1) + v2  # Apply linear transformation and add an initialized tensor to the output of the linear transformation
        return v5
 
    def _linear_transformation(self, x): 
        v3  = torch.randn(90, 784, 6).long() * x
 
        return v3 


# Initializing the model
m  = Model()
 
# Inputs to the model