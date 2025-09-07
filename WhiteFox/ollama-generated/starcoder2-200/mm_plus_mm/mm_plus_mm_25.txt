
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1,y2) # matrix multiplication of two matrices
        v2  = torch.mm(x3,y4) # matrix multiplication of three matrices 
        v3  = v1 + v2  # addition of two results
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(500, 789)# matrix input one
y1 = torch.randn(456, 987) # matrix input two 
z1 = torch.randn(321, 978) # matrix input three


__output__=m(x1, y1), z1)

