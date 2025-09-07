
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.permute(x1, (0, -1)) # swap 1 and 3 dimensions of the input tensor A 
        v2  = torch.bmm(v1, torch.permute(x2, (-1, 0))) # swap 2 and 4 dimensions of the input tensor B
        return v2

# Initializing the model
m = Model()


# Inputs to the model: 
x1 = torch.randn(3)
x2 = torch.randn(2, 3)
__output__  = m(x1, x2)

