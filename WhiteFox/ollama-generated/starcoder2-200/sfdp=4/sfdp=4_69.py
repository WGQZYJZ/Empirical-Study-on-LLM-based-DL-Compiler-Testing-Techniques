
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v = (query1 @ key2.transpose(-2, -1)) / math.sqrt(query1.size(-1)) + attn_mask 
        w  = torch.softmax(v, dim=-1)
        out = w @ value3  
        return out

m  = Model()

 # Inputs to the model
qk  = torch.randn(4096, 256) 
 key2  = torch.randn(4096, 256)
value3  = torch.randn(1785, 4096, 256) 
attn_mask  = torch.randint(0, 2, (4096,))
 
# Attention mask 
attn_mask  = attn_mask > 0 

# Run forward 
x1 = m(qk, key2, value3)

