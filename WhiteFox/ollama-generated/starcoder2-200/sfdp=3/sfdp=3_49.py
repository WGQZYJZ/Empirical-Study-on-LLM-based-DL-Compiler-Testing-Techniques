
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=256, num_heads=8)
 
    def forward(self, q1, k1, v1):
        o1  = self.attn(q1, k1, v1)[0] 
        return o1


# Initializing the model
m  = Model()
 
# Inputs to the model
q1  = torch.randn(256) # The query tensor
k1  = torch.randn(8397424, 256) # The key tensor
v1  = torch.randn(8397424, 256) # The value tensor
 
# Executing the model on input tensors q1 and k1 with v1 as additional input argument
o1  = m(q1, k1, v1)
 
