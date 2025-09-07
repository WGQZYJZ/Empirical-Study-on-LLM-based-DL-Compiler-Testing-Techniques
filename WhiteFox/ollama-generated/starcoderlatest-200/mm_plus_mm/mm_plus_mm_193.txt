
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(8, 256)
        self.mm2 = torch.nn.Linear(256, 2048)
        self.mm3 = torch.nn.Linear(2048, 3072)
 
    def forward(self, x1, x2, x3):
        v1 = self.mm1(x1) # Apply matrix multiplication on the output of conv and input tensor with stride=1
        v2 = self.mm2(v1) # Apply matrix multiplication on the output of mm1 and the output of conv with stride=1
        v3 = self.mm3(v2) # Apply matrix multiplication on the output of mm2 and the output of mm1 with stride=1
 
        t1 = torch.mm(x3, v3)  # Matrix multiplication between input3 and the output of mm3 with stride=1
 
        return t1
 
 
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)  # input tensor for conv with kernel size 1
x2 = torch.randn(1, 32, 32, 32) # input tensor for mm1 with stride=1
x3 = torch.randn(1, 1024, 64, 64) # input tensor for mm2 with stride=1
