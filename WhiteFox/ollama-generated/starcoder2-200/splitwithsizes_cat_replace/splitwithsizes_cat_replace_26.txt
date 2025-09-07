
class Model(torch.nn.Module):
    def __init__(self, splitdim=0):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.split(x1, [32], dim) # Split the input tensor along dimension 0 into several tensors of size 32.
        v2  = torch.cat([v1[i] for i in range(len(v1))], dim=0) 
        return v2

m = Model()

x1  = torch.randn(4, 896, 75, 75) # create a random input tensor of shape (4, 896, 75, 75)

