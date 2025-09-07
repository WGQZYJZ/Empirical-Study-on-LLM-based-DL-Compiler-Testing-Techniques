
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other=None): # In PyTorch, keyword arguments are denoted by 'other='
        v1  = self.conv(x1)
        v2  = v1 + other 
        return v2

# Initializing the model with a non-default value for one of the keywords.
m  = Model()

