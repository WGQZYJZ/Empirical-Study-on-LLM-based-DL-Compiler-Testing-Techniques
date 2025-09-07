
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 3, 4) # Permute the input tensor A (x1), it is 5 dimensions.
        v2  = x2.permute(1, 2, ...) # Permute the input tensor B (x2). The permute method should have 3 more dimensions than before. The first two dimensions are swapped and then the third dimension will be appended to the back of the tensor
        v3  = torch.bmm(v1, v2) # or torch.matmul(v1, v2) 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 5, 4) # A.dim() == 5 (tensor A. The permute method swaps the third and fourth dimension of it. So the dim() will become 4 instead of 5.)
x2 = torch.randn(4, 3)


__output__  = m(x1, x2)

