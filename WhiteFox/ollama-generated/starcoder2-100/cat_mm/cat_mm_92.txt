
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.mm(x1)
        t2  = torch.cat([t1])
        return t2

 # Initializing the model<|end_of_code|>
m  = Model()
 
 # Inputs to the model<|end_of_code|>
input1  = torch.randn(64, 3, 3)
input2  = torch.randn(64, 78)
 
__output__  = m(x1)

