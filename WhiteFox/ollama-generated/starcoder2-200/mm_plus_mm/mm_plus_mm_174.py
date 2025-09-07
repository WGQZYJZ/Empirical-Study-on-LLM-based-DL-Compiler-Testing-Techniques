
class Model(torch.nn.Module):
    def __init__(self, d1=4096, d2=4096):
        super().__init__()
        self.input1 = torch.nn.Linear(d1, d1)
        self.input2 = torch.nn.Linear(d1, d2)
        self.output1 = torch.nn.Linear(d2, 5)
 
    def forward(self, x):
        v1  = self.input1(x) # Apply matrix multiplication to the input tensor using an internal weight matrix as input to this operation.
        v2  = self.input2(v1) 
        v3  = torch.mm(v1, v2.t()) # Matrix multiplication between inputs resulting from previous operations that use a weight matrix and a transposed version of itself.
        return v3

m  = Model()

x1 = torch.randn(8096).unsqueeze(-1)
x2 = torch.zeros_like(v1)
