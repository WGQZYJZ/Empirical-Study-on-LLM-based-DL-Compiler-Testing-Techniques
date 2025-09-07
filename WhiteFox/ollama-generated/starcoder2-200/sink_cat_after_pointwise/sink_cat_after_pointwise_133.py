
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3) # linear transformation to generate two matrices with 3 rows and 4 columns.
        self.linear2 = torch.nn.Linear(4, 6)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1) # the second linear transformation is used on a pointwise unary operation applied after the concatenation of two tensors
        v3 = torch.nn.functional.relu(torch.cat([v1, v1], 1)) # Concatenate tensors along dimension 0 and apply ReLU to it.
        return v2

# Initializing model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 4)

