
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.25) # Dropout with probability 0.25 is invoked on the input tensor
        v2 = torch.rand_like(x1) # Generate a random tensor filled with numbers from -1 to 1 
        return v1 + v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4)
