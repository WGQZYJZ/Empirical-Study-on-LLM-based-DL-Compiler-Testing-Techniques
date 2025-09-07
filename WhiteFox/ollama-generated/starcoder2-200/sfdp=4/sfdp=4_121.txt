
class Attention(torch.nn.Module):
    def __init__(self, dim1: int=4096, dim2: int=4096) -> None
        self.query = torch.nn.Linear(dim1, dim2) 
        self.key = torch.nn.Linear(dim1, 4096) 
        self.value = torch.nn.Linear(dim1, dim2) 
 
    def forward(self, query):
        attn_mask = torch.full((query.size(-2), query.size(-3)), -float('inf')) # Define the attention mask as a full matrix filled with -∞
        mask_indices  = torch.where(attn_mask == float('inf'))  # Retrieve the indices of the mask elements where the value is +∞, and store them in "mask_indices"
 
        attn_weight = self._scaled_dot_product_attention(query, key=self.key(query), value=self.value(query))  # Compute the scaled dot product attention weights using the private method "_scaled_dot_product_attention()"
        attn_weight[mask_indices] = float('nan') # Set the attention mask elements in "mask_indices" to NaN
        output = torch.softmax(attn_weight, dim=-1)  # Compute the softmax of the attention weights
        
        return self._scaled_dot_product_attention(query, key=self.key(query), value=self.value(query), attn_weight=output)
 
    def _scaled_dot_product_attention(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_weight: torch.Tensor=None) -> torch.Tensor
        scale = 1 / math.sqrt(query.size(-1))  # Compute the scaling factor for the dot product
        return (query @ key.transpose(-2, -1).to(query.device) * scale) + attn_mask


# Initializing the model
model  = Attention()
 
