
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attn  = torch.nn.MultiheadAttention(128, 8)
 
    def forward(self, query, key, value):
        attn_mask  = torch.zeros((query.size(0), value.size(-3), 512), device="cuda") 
        attn_mask.masked_fill_(attn_mask != 0 , -float("inf"))
        v1  = self.attn(query, key + attn_mask)
        v2  = torch.softmax(v1[1], dim=1)
        return v2 @ value


# Initializing the model
m = Model()

 # Inputs to the model
 query  = torch.randn((50,384), device="cuda")
 key   = torch.randn((query.size(0), 512), device="cuda") 
 value  = torch.randn((key.size(-1)), device="cuda")
 
__output__  = m(query, query + attn_mask ,value)

- The model should contain two MultiheadAttention layers. In the second MultiheadAttention layer, there is a mask for each query (or sequence of queries) in the batch. That is, it contains the same length as every input (the query). Since each query has a different number of output tokens (which are not necessarily the same), this means that there will be one mask per query. There can also be several queries with one mask.
- The masks need to be in the shape `(n, m)` where `m` is the maximum length of any query sequence and n is the batch size.