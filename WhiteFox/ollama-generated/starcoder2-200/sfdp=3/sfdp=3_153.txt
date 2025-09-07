
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.Tensor([1])
 
    def forward(self, query, key, value):
        self.scale  = torch.rand(()) * 20 + 5 
        vq = query.matmul(key)
        vqk  = vq.mul(self.scale)
        vsqk = vqk.softmax(-1).dropout(p=0.4)
        vo = vsqk.matmul(value)
        return vo


# Initializing the model
m  = Model()

# Inputs to the model
query, key, value  = torch.randn(32, 64),torch.randn(32, 64),torch.randn(32, 8192)
__output__   = m(query, key, value)