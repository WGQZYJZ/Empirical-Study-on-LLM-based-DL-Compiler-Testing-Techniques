
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
 
        # Subtracting an array from the output of a linear transformation
        v2 = v1 - other_arr
 
        return v2
 
# Initializing the model and generating the input tensor
m = Model()
x1  = torch.randn(5, 10)
other_arr = torch.randn(3, 4) * 0.7 + m.linear.bias.item()
 
  # Input to the model: a 2-dimensional matrix of shape (5, 10), representing some data points
  