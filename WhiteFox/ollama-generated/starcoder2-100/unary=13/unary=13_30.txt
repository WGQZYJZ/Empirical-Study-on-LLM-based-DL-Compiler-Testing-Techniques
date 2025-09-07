
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(1024, 1)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = torch.sigmoid(v1) 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(30, 5408) # The shape of the input tensor is (N x d), where N is the batch size and d is the dimensionality of each vector.
__output__  = m(x1)

