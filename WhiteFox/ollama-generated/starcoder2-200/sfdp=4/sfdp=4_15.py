
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
 
        v1  = self.attn(input1)
 
        v2  = torch.softmax((v1 + v1).transpose(-2, -1), dim=-1) @ v1 # compute the softmax of the result
 
        v3  = torch.sum(v2*v1,dim=1) # compute a sum of the weighted values

        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(8,64)
__output__  = m(x1, x1)


