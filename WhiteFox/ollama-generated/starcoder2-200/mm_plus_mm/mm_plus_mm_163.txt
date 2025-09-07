
class Model(torch.nn.Module):
    def __init__(self, in1=3, in2=4):
        super().__init__()
        self.mm = torch.nn.Linear(in1*in2, 10)
 
    def forward(self, x1, y1, z1):
        v1  = torch.mm(x1, y1) # Matrix multiplication between input_tensor1 and input_tensor2 
        v2  = self.mm(z1).T 
        v3  = v1 + v2   # Addition of the results of two matrix multiplications
        return v3

m=Model()
__output__  = m(x, y, z)

