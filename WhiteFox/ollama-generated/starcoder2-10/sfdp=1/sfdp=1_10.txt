
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 32
        self.key = torch.randn(10, 4) * 500 + 100
        self.query = torch.randn(8, 16)
        self.value = torch.randn(8, 7, 9)
 
    def forward(self):
        vq  = torch.matmul(self.query, self.key.transpose(-2, -1))
        scf  = (self.scale ** (-0.5)).expand_as(vq)
        vsf  = vq * scf
        vsof  = vsf.softmax(dim=-1) 
        vdf  = torch.nn.functional.dropout(vsof, p=0.8) 
        vout  = vdf.matmul(self.value) 
        return vout


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(2, 16)
k  = torch.randn(3, 4) * 50 + 10
v  = torch.randn(9, 7)
__output__  = m(q, k, v)

