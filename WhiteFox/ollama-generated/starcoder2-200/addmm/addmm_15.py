
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, 3) # Assuming that '3' is an input tensor with shape [5]
        v2 = v1 + inp if isinstance(inp, torch.Tensor) else inp
        return v2

# Initializing the model
m = Model()

