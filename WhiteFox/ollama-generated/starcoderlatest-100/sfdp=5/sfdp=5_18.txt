
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(embed_dim=8, num_heads=1)
 
    def forward(self, query, key, attn_mask):
        output = self.attention_layer(query, key, value, attn_mask) # This operation computes the attention weights and the output
        return output
 
class SelfAttentionLayer(nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.dim = dim
 
    @staticmethod
    def apply_attention(query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor]:
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        if attn_mask is not None:
            qk += attn_mask  # Add the attention mask to the scaled dot product

        attn_weights = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weights @ value  # Compute the dot product of the dropout output and the value
        return output
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, attn_mask: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor]:
        output = SelfAttentionLayer.apply_attention(query=query, key=key, value=value, attn_mask=attn_mask)  # Compute the attention weights and the output
        return output
# Inputs to the model
q1 = torch.randn(1, 8, 64, 64)
k1 = torch.randn(1, 8, 64, 64)
v1 = torch.randn(1, 8, 64, 64)
attn_mask1 = torch.tensor([[0.,  0.,  0., ..., 0., 0., 0.],
                           [0.,  0.,  0., ..., 0., 0., 0.],
                           [0.,  0.,  0., ..., 0., 0., 0.],
                           ...
                           [0.,  0.,  0., ..., 0., 0., 0.]], dtype=torch.float, device="cpu")
