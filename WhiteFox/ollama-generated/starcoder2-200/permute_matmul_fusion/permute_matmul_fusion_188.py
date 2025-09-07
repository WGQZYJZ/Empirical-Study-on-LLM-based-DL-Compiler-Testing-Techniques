
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v1  = torch.randn(3, 4) 
        v2  = torch.randn(5) # input tensor B
        v3  = v1.permute(0, 2, 1)
        v4  = torch.bmm(v3, v2)
        v6  = v1.permute(0, 1, 2)

        return v4, v5


# Initializing the model
m = Model()

 # Inputs to the model
x1_1 = torch.randn(7, 8) # input tensor A
x1_2 = torch.randn(9)    # input tensor B
__output__, __output___ = m(x1_1, x1_2)