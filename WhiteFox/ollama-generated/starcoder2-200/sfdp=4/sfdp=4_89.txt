
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.temperature = 8.0

    def forward(self, query: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
        # Compute the dot product of the query and key matrices using torch.einsum
        qk_matmul = torch.einsum("...ij,...jk->...ik", [query, key])

        # Scale the dot products by dividing with sqrt(dk) to prevent their explosion 
        scaled_dot = nn.functional.normalize(qk_matmul / self.temperature)
    
        # Add the attention mask for padding or causal effects
        scaled_dot += attn_mask

        # Apply softmax over the last dimension of the matrix (dim=2), and then multiply by value to get attention weights as a weighted sum
        attn = nn.functional.softmax(scaled_dot, dim=-1)
        attn_applied = torch.einsum("...ij,...jk->...ik", [attn, value])

        return attn_applied

# Initializing the model
model  = ScaledDotProductAttention()

 # Inputs to the model
    query  = torch.randn(64, 256)
     key   = torch.randn(30000, 19872) 
     value = torch.randn(30000, 3000)
     attn_mask = torch.full((query.shape[1], key.shape[1]), float('-inf'), device=query.device).triu()

 # Generating attention weights for each query/key pair using model
 __output__  = model(query, key)


