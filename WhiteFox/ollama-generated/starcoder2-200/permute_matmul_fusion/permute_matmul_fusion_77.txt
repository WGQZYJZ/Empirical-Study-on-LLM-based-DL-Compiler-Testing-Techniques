

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): # The model must have 2 input tensors
        v1 = torch.bmm(x1.permute(0, 3, 1, 2), x2) # swaps 1 and 4 dimensions of the tensors.
        return v1


m  = Model()

x1_A  = torch.randn(16,  8,   15 ,   9 )
x2_B  = torch.randn(10, 23) # The 3rd dimension of input tensor B must be the same as 4th dimension of input tensor A
__output__  = m(x1_A, x2_B)

