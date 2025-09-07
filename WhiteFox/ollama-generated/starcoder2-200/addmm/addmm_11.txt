
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1=None, inp=0.5):
        if not isinstance(x1, torch.Tensor):
            raise ValueError('Expected 2D torch Tensor for input.')

        v1 = torch.mm(inp, torch.zeros(784, 784))
        v2 = v1 + x1

# Initializing the model
m = Model()

