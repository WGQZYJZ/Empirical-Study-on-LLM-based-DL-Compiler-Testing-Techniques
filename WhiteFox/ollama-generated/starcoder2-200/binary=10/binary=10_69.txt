
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       v0 = self._linear(x1) # Calling a custom function on the input tensor
       v1  = torch.add(v0, 2 * torch.ones_like(v0))# Add another tensor to the output of the linear transformation
       return v1

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 5)
__output__  = m(x1)