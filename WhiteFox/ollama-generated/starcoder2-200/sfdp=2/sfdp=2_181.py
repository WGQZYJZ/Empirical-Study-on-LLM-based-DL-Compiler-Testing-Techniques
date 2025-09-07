
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        vq  = torch.matmul(query1, key1.transpose(-2, -1))
        vsc = vq / 0.75
        vsft = vsc.softmax(dim=-1) 
        vsdo = vsft + 0.42
        vo = vsdo.matmul(value1)
 
        return vo


# Initializing the model
m = Model()

# Inputs to the model
q1, k1, v1 = torch.randn(3), torch.randn(5), torch.randn(7)
__output__  = m(q1, k1, v1)
