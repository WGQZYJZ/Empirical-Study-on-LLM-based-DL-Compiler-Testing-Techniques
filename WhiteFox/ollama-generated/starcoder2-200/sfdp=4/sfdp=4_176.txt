

class DotProductAttention(torch.nn.Module):
    def __init__(self, attn_mask):
        super().__init__()
        self.attn_mask  = attn_mask
 
    def forward(self, query, key, value):
        qk  = torch.einsum('...qlhd, ...khbd->...qlhb', query, key) / math.sqrt(query.size(-1))
        qk += self.attn_mask
        attn_weight  = torch.softmax(qk, dim=-1) 
        output  = torch.einsum('...qlhb,...hlb->...qlhd', attn_weight, value)
 
        return output
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask  = torch.zeros([8,128], dtype=torch.float32).fill_(float('-inf'))
        self.dotproductattention  = DotProductAttention(self.attn_mask)
 
    def forward(self, query, key):
        value  = query  # Replace this with your model's output tensor
        output  = self.dotproductattention(query=query,key=key,value=value)
 
        return output


# Initializing the model
m  = Model()

# Inputs to the model
key1  = torch.randn([8,4096]) # Replace this with your key tensor
query2  = m(key1)

