
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) + self._other
        v2  = torch.relu(v1)
        return v2

 # Initializing the model
 m = Model()
 
# Inputs to the model (without an other)
x1 = torch.randn(3, 5)
 
__output_without_other__ = m(x1)
 
# Now, inputs with the "other" tensor
x2 = torch.randn(4, 8)
y2 = torch.randn(4, 7)
 
