
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask):
        v1  = torch.einsum("abcde, fge->abefg", (query, key))
        v2  = v1 / math.sqrt(query.size(-1)) 
        v3  = v2 + attn_mask 
        v4  = torch.softmax(v3, dim=-1) 
        v5  = torch.einsum("acefg, cegh->abefg", (v4, value))
        return v5


# Initializing the model
m  = Model()


# Inputs to the model
query_input  = torch.randn(32, 8, 64)
key_input    = torch.randn(32, 8, 64)
value_input  = torch.randn(32, 1024, 768)
attn_mask_input   = torch.randn(query_input.size()) > -9e-8


# Output of the model
m(query_input, key_input, value_input, attn_mask_input)

