
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, a2):
        v1  = torch.mm(x1, y1) 
        v2  = torch.mm(z1, a2) # Matrix multiplication between two tensors.
        return v3  + v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn([8, 5]) # Tensor with 8 rows and 5 columns.
y1  = torch.randn(8) 
z1  = torch.randn(50, 32)
a2  = torch.randn(64, 1024)


__output__  = m(x1, y1, z1, a2)
