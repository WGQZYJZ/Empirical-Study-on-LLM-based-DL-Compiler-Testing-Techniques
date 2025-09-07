

class Attention(torch.nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.scale = 1 / math.sqrt(dim)

    def forward(self, query: torch.Tensor, key: torch.Tensor, attn_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        qk = query @ key.transpose(-2,-1) * self.scale

        if attn_mask is not None:
            qk += attn_mask
            
        # Compute the softmax for attention weights and apply dropout to the result
        attn_weights = torch.softmax(qk, dim=-1).masked_fill(attn_mask == 0., -1e9)
        attn_weights = torch.dropout(attn_weights, 0.1, True)

        # Compute the dot product of the dropout output and value to get output 
        output = attn_weights @ key
        
        return output

m = Attention(512)

query = torch.rand(48, 64*7*7, dtype=torch.float32)
key = torch.rand(48, 64*7*7, dtype=torch.float32)
attn_mask = None
output = m(query, key, attn_mask)

