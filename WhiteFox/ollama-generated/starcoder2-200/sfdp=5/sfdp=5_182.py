
class Attention(torch.nn.Module):
    def __init__(self, d_model=256):
        super().__init__()
        self.d_model  = d_model
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor,
                attn_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        if attn_mask is not None:
            qk  = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight  = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output  = attn_weight @ value 
        return output


# Initializing the model
attn = Attention()


