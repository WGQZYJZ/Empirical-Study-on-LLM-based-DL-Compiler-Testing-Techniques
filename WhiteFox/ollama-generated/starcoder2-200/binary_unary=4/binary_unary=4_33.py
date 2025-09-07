
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(2, 3) # Other tensor for the pattern
        v1 = self.linear(x1 + v0) 
        return v1

# Initializing the model
m  = Model()
__output___ = m(torch.randn(2, 5))

