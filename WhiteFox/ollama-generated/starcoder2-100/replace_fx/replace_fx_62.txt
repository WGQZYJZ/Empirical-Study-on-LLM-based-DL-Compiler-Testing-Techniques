
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1) 
        v2  = torch.rand_like(v1) # generate a tensor with the same size as input_tensor filled with random numbers
        return v2

m  = Model()
x1 = torch.randn(3,4)

