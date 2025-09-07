
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q, k, v):
        m  = torch.matmul(q, k.transpose(-2, -1)) 
        r  = m * scale_factor
        s  = r.softmax(dim=-1)
        d  = torch.nn.functional.dropout(s, p=dropout_p) 
        o  = v.matmul(d)
        return o

# Initializing the model
model  = Model()

 # Inputs to the model 
 q0 = torch.randn(256, 384).to('cuda')
 q1 = torch.randn(256, 384).to('cuda')
 q  = torch.cat([q0, q1], dim=0)
 k  = torch.randn(768, 384).to('cuda')
 v  = torch.randn(768, 256).to('cuda')

 # Inputs for the dropout and softmax layers 
 p0 = torch.rand([1]) + 5e-4
 p1 = torch.rand([1]).add(5e-3)

 # Forward pass
 