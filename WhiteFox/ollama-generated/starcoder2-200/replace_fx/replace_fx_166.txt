
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        # Erase these nodes to generate a graph
        v  = torch.nn.functional.dropout(input1) 
        v2 = torch.rand_like(v)
        v3 = torch.rand_like(v)
        return v + v2 + v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 2)
x2  = torch.randn(2, 4)

m(x1, x2)