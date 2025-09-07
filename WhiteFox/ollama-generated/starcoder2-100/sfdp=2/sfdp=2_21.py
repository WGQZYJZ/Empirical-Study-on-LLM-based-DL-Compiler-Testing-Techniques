
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(8, 1)
 
    def forward(self, x1):
        v1  = self.att(x1, query=x2)[0]  # Apply multihead attention to the inputs and return only the output of the dot product of a query and a key without applying dropout or scaling
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(32, 80, 5)
x2  = torch.randn(32, 5, 64)
__output__  = m(x1)

