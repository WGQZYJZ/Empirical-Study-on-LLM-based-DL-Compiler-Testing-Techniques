
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> Tuple[torch.Tensor]:
        # Compute the dot product of the query and key tensors
        qk = torch.einsum('bnhwc,bkhwd->bnhd', [query, key])
 
        # Add the attention mask to the scaled dot product
        attn_mask = torch.zeros(qk.shape)  # Initialize a zero-filled attention mask
        attn_mask[:, :, 0: query.size(-1), :] = -9e5 
        attn_mask[:, :, key.size(-2):, :] = -9e5
        attn_mask = torch.where(attn_mask != -9e5, qk + attn_mask, qk)
 
        # Compute the attention weights as softmax of the scaled dot product
        attn_weight = F.softmax(attn_mask / math.sqrt(query.size(-1)), dim=-1)
 
        # Use the attention weights to compute a weighted sum of the value tensor
        output  = torch.einsum('bnhd,bkhwd->bnhwc', [attn_weight, value])
        return output


# Initializing the model