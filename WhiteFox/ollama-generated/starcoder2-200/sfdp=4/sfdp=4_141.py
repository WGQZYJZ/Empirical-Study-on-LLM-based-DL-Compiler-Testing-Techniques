
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask=None) -> torch.Tensor:
        # Compute the dot product of the query and key tensors, and scale it by the square root of the size of the query vector
        k_T  = key.transpose(-2,-1).contiguous() 
        dq  = query @ k_T / math.sqrt(query.size(-1))
 
        # Masking
        if mask is not None:
            assert mask.dim()==dq.dim()-2, "Mask shape mismatched" 
            dq += mask
        # Apply softmax to the result
        dq = nn.functional.softmax(dq)
 
        # Compute the dot product of the attention weights and value tensor 
        out  = torch.einsum("...aj,...bj->...ij", dq, value).contiguous()
 
        return out, dq

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
        self.attention = ScaledDotProductAttention().cuda()
 
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        return self.attention(x1, key=x2, value=x3).cuda()

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn((batch_size, embed_dim)).cuda() # The query tensor
key = torch.randn([2048*7*7,embed_dim]).view(368640 , 96).float().cuda() # The key tensor
value = torch.randn([2048*7*7,embed_dim]).view(368640, 96) .float().cuda() # The value tensor
 
__output__  = m(x1)

