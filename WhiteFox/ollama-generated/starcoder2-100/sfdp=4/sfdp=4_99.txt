
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, attn_mask: torch.Tensor) -> torch.Tensor:
        qk = query @ key.transpose(-2,-1)/ math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, and scale it by dividing each row by the square root of its size minus one (the size is equal to the batch size multiplied by the feature dimension)
        qk = qk + attn_mask  # Add the attention mask to the scaled dot-product
        attn_weight = torch.softmax(qk, dim=-1)  # Compute the attention weights as the softmax of the scaled dot product
        output = attn_weight @ value  # Compute a weighted sum using the attention weights and the value tensor 
        return output


# Initializing the model
sa = ScaledDotProductAttention()
 
 # Inputs to the model
 query = torch.randn(2, 8)
 key = torch.randn(10, 7)
 attn_mask = torch.ones((4, 5))
 __output__  = sa(query, key, attn_mask)

 