
class Model(torch.nn.Module):
    def __init__(self, m: int):
        super().__init__()
        self.m  = torch.nn.ParameterList([
            torch.nn.Linear(8 * 64 ** 2, 3), 
            torch.nn.Linear(3, 10)
        ])
        
    def forward(self, x1, y1):
        v0  = torch.cat((x1[:,None],y1[None,:]), dim=0)
        v1 = self._modules["m"][0](v0)
        v2 = v1 + x1 
        v3 = [torch.norm(v2)] # norm of the output of concatenation of input 1 and input 2
        v4 = torch.softmax(self.m[0], dim=None) # softmax on input 1 after concatenation
        v5 = torch.nn.functional.sigmoid(self._modules["m"][1](torch.cat((v3, y1),dim=0))) # sigmoid function of the output 
        return [torch.nn.functional.linear(x1, x2) for x1, x2 in zip(y1.T, self.m)]

# Initializing the model
m = Model()


# Inputs to the model
input1  = torch.randn(320,8*64**2); input2  = torch.randn(320)
output__ = m(input1 , input2) # output is a list of three tensors

