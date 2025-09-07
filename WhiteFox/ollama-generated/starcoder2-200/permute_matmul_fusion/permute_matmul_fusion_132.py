
class Model(torch.nn.Module):
    def __init__(self, insize = 2, outsize=3):
        super().__init__()
        self.linear1 = torch.nn.Linear(insize, insize)
        self.linear2 = torch.nn.Linear(insize, outsize)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous() # Permuted tensor A
        v2 = x2.permute(0, 2, 1).contiguous() # Permuted tensor B
        v3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2) 
        v4 = self.linear1(v3) # Linear transformation on the permuted tensors
        return self.linear2(v4), v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 5, 7)
x2 = torch.randn(3, 8, 6)

__output__  = m(x1, x2).type('torch_tensor')

