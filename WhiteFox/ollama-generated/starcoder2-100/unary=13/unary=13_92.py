
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 32)
        self.sigm = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.sigm(v1)
        v3 = v1 * v2 # gate 1
        return v3

m  = Model()


x1 = torch.randn(50, 20)# shape of the input tensor, which needs to match that of the input_tensor in the forward method
__output__  = m(x1) #shape of __output__, which is expected to match that of the output of the forward method

