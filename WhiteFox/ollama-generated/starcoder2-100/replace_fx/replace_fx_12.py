
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5) # Apply dropout to the input tensor 
        return torch.rand_like(v1, 1.)


# Initializing the model