
class AttentionBlock(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.linear1  = torch.nn.Linear(hidden_size, hidden_size)
 
        self.norm2  = torch.nn.LayerNorm(hidden_size)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        k_prime  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        k_prime  = k_prime + attn_mask  # Add the attention mask to the scaled dot product
 
        k_weight  = torch.softmax(k_prime, dim=-1)  # Apply softmax to the result
        k_weight  = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
 
        output  = attn_weight @ value
 
        return self.norm2(self.linear1(output))


# Initializing the model
mb  = AttentionBlock(8)


# Inputs to the model