
class Attention(torch.nn.Module):
    def __init__(self, attn_config: dict) -> None
        self.dropout = torch.nn.Dropout(**attn_config["dropout"])
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask: Optional[torch.Tensor] = None):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it 
        if not mask is None:
            qk += mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        if not self.training or not dropout_p:
            attn_weight = self.dropout(attn_weight) # Apply dropout to the softmax output
        return attn_weight @ value # Compute the dot product of these attention weights and the value


# Initializing the model
attn  = Attention({"dropout": {"probability": p}})
 
 # Inputs to the model
query  = torch.randn(32, 64)
key    = torch.randn(32, 1024, 8, 15).reshape(-1, 1024 * 8)
value   = torch.randn(32, 1024, 8, 15).reshape(-1, 1024*8)
attn_mask  = torch.randint(low=0, high=9, size=(32, 64), dtype=torch.float).abs() > 0 # Generate a randomly shaped mask for the attention mechanism to avoid using information from future tokens
 
 