
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.rand_like(x1) # Generate a tensor with the same size as input filled with random numbers
        t3 = torch.nn.functional.dropout(t2, 0.5) # Apply dropout to this tensor
        return t3

# Initializing the model
m = Model()

# Input tensors of the model
x1  = torch.randn(1, 2, 3)

