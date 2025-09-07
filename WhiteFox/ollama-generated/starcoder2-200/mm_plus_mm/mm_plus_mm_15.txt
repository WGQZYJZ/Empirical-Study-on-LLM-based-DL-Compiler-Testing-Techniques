
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v0 = torch.mm(x1, y1)
        return 3*v0, 2*y1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4,8)
__output__, __output_y__ = m(x1, x1) # This model takes two input tensors of the same size as the inputs of the previous model

