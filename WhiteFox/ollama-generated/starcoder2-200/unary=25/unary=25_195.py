
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear  = torch.nn.Linear(8 * 64 * 64, 9)
 
    def forward(self, x): 
        v1  = self.linear(x)
        v2  = (v1 > 0).type_as(v1)
        v3  = negative_slope*v1
        v4  = torch.where(v2, v1, v3)
        return v4

 # Initializing the model
m = Model()
negative_slope=0.5
# Inputs to the model
x1 = torch.randn(7 * 8 * 64* 64).view(-1, 7 * 8 * 64 , 64)
__output__  = m(x1)

