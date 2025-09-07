
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.rand(3) - other # Subtract  'other' from the input of rand
        v2 = torch.tensor([x for x in [-4., 5., 6.]], dtype=torch.float32) - other # Subtract  'other' from a list containing [-4, 5, 6]
        v1 = torch.randn(4) + other # Add  'other' to the output of randn
        v3 = torch.tensor([x for x in [7., -8., -9., 0.,]], dtype=torch.float32) + other # Add  'other' from a list containing [-4, 5, 6]
        return (v1 * v2).sum()


# Initializing the model
m = Model(0.)
 
# Inputs to the model
x1 = torch.randn(1)
__output__  = m(x1)