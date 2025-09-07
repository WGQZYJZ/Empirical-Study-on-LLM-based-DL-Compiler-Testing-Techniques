
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.nn.functional.dropout(x1, self.p) # Apply dropout to the input tensor. 
        v3 = torch.rand_like(v2, self.p)               # Generate a random tensor with same size as input and set all elements to p.
        return v3


# Initializing the model