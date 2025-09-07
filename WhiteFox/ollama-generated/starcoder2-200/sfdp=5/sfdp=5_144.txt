
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dmodel=768):
        super().__init__()
        self.dmodel = 120
 
    def forward(self, query, key, value):
        attn_mask  = torch.zeros(query.size()).to(query)
        attn_weight  = query @ key.transpose(-2,-1)/math.sqrt(self.dmodel) 
        attn_weight  += attn_mask # add mask
        attn_weight = torch.softmax(attn_weight,dim=-1)
        output = attn_weight @ value
        return output


m = MultiHeadAttention()
 
query  = torch.randn(32*768)
key  = query
value = key
 
attn_output  = m(query=query,
                 key=key,
                 value=value,
                )
