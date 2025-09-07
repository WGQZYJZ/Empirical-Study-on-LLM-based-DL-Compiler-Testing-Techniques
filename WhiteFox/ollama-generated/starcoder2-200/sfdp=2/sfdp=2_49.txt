
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(data=torch.tensor([1.0 / math.sqrt(3)]))
 
    def forward(self, q, k, v):
        out_1  = torch.matmul(q, k.transpose(-2, -1))
        out_2  = out_1.div(self.scale)
        out_3  = out_2.softmax(dim=-1)
        out_4  = out_3.dropout(p=0.5, training=True)
        out_5  = torch.nn.functional.dropout(out_4, p=0.7)
        return out_5.matmul(v), out_2


# Initializing the model
m = Model()
 
# Inputs to the model
q  = torch.randn(1, 64, 3)
k  = torch.randn(1, 8, 3)
v  = torch.randn(1, 64, 32)
 
  __output__, out_2  = m(q, k, v)
 
 
