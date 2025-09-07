
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
         v1  = torch.bmm(query / torch.sqrt(query.size(-1)),  key.transpose(-2,-1))
         v1 += attn_mask 
         v2  = torch.softmax(v1, dim=-1) # (..., query_length, key_length)
         v3  = torch.bmm(v2, value) # (..., query_length, value_length)


# Initializing the model