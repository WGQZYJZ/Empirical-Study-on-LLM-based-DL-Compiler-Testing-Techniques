
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.mm
 
    def forward(self, x1, x2):
        v1  = self.mm(x1, x2) 
        v2  = torch.cat([v1 for i in range(7)], 0) # Concatenate the matrix multiplication result along dimension 0 seven times
        return v2


# Initializing the model
m  = Model()
__output__  = m(torch.randn(3,5), torch.randn(5,8))