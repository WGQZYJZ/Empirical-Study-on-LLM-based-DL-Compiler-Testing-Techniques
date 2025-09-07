
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.nn.functional.dropout(x1, 0.5) # This dropout node will be erased from the graph. 
        # Replace this line with "v2  = torch.rand_like(x1)" to replace the dropout operation.
        v3 = x1 + 1
        return [v0, v3]

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5)
