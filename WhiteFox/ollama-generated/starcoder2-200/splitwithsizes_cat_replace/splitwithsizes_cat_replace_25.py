
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1, v2, v4, v5  = [self.split(x1)] * 4 # Split the input tensor into four tensors along dimension 0 
        # Concatenate these split tensors along dimension 0 in the reverse order to their original order during the concatenation operation

        __return__ True if (v1 == v2).all() and (v3 == v5).all() else False

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 64)

