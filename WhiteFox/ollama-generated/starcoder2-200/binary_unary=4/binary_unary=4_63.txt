
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other=None):
        v1 = self.linear(x1) # Apply linear transformation to input tensor
        if other is None:
            return v1 
        else: 
            return v1 + other # Add another tensor to output of the linear transformation

# Initializing model and passing keyword argument 
m = Model()

