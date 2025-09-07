
class Attention(torch.nn.Module):
    def __init__(self, qkv_head_dim: int = 64) -> None:
        super().__init__()
 
        self.k = torch.nn.Parameter(torch.Tensor(32768, 900)) # Initialize a 32768-by-900 parameter
        self.v = torch.nn.Parameter(torch.Tensor(32768, qkv_head_dim))
 
    def forward(self, query: torch.Tensor):
        qk  = query @ self.k.transpose(-2,-1) # Compute the dot product of the query and key
        qk  += self._attn_mask() # Add an attention mask to the scaled dot product output
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax on the resulting dot product
        attn_weight = torch.dropout(attn_weight, .3, True) 
        out  = attn_weight @ self.v
        return out 
 
    def _attn_mask(self):
        # Make a 32768-by-900 attention mask to block the dot product of self with itself
        mask  = torch.zeros((32768, 900), device=torch.device("cuda:1")) 
        for i in range(mask.size(-1)):
            mask[i, i]   = -float('inf')
        return mask
 
class Model(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.attn  = Attention()
 
    def forward(self, input_: torch.Tensor):
        return self.attn(input_)
 
 
# Initializing the model
model  = Model()
 
# Input tensor to the model
input_tensor = torch.randn((1024,), device=torch.device("cuda:0"))

