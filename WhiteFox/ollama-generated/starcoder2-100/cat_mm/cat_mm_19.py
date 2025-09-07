
class Model(torch.nn.Module):
    def __init__(self, input1 = torch.randn((10)),input2=torch.randn((5)) ):
        super().__init__()
 
    def forward(self, x1):
 
        v1  = torch.mm(x1 , x1) 
        v2 = v1 * 4
        v3  = torch.cat([v1, v1], dim=0)
        return v2, v3


# Initializing the model and generate inputs to the model
m = Model()
x1  = [
    torch.randn(5),
    torch.randn(7)]
 
__output__, out2 = m(x1)

