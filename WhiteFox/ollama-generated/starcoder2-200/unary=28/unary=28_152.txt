
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.)
        super().__init__()
        self.linear = torch.nn.Linear(in_features=32 * 32 * 3, out_features=4)

    def forward(self, x): 
        v1 = self.linear(x) # Apply a linear transformation to the input tensor
        v2 = torch.clamp_min(v1, min_value=0.) # Clamp the output of the linear transformation to a minimum value (minimum is 0 in our case)
        v3 = torch.clamp_max(v2, max_value=4.) # Clamp the output of the previous operation to a maximum value 
        return v1

# Initializing model
m = Model()
__input_x1__ = torch.randn(500, 32 * 32 * 3) # The input tensor for our example should be 500 x 9216-element vector 
__output___ = m(__input_x1__)
