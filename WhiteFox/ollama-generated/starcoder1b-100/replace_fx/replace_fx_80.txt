
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.functional.dropout

    def forward(self, x1):
        v1  = self.dropout(x1) # Erase the original call of 'torch.nn.functional.dropout' in the graph
        v2  = self.rand_like(v1, 100)   # Generate a random number with 100 elements and return as the new input
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
