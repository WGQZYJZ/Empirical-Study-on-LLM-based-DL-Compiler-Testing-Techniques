
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        v1  = torch.einsum("ab, bc->ac", query, key) 
        v2  = v1 / math.sqrt(query.size(-1)) # Scale the dot product of the query and key tensors using the square root of the number of columns in the query tensor. 
        v3  = v2 + attn_mask
        attn_weight  = torch.softmax(v3, dim=-1)
        output  = torch.einsum("ab, bc->ac", attn_weight , value )
        return output
 
 # Initializing the model
m  = Model()
 
 
 # Inputs to the model
 query = torch.randn(8,4096) 
 key = torch.randn(257*3 *3,  16).reshape(-1, 4096)  
 attn_mask = torch.randn(query.shape[0], key.shape[-2], key.shape[-1])
__output__  = m(query,key ,attn_mask)
 
