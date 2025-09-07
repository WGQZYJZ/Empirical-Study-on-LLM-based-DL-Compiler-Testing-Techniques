
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.nn.functional.linear(x1) # Apply linear transformation to the input tensor A.
        v2  = torch.nn.functional.linear(v1) # Apply linear transformation to the output of applying the first linear transformation to the input tensor A.

        v3  = x2.permute(0, 2, 1).bmm(v2) # Permute and bmm the input tensors B and the previous linear transformation's output
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1_1  = torch.randn(10, 5, 4)   # A.shape=(batch size x 5 dimensions x 4 dimensions)
x1_2  = torch.randn(3, 5)        # B.shape= (3 elements x 5 dimensions) 

x2  = torch.randn(8, 7, 6)       # C.shape=(batch size x 7 dimensions x 6 dimensions)
__output__  = m(x1_1, x1_2, x2)

