
class MultiHeadAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 128)
 
    def forward(self, q_t, k_t, v_t, attn_mask=None):
        v_t = self.qkv(v_t).reshape((32, -1, 16)) # Reshape to (batch_size, num_heads * hidden_dim, seq_length, embed_dim // num_heads)
        q_t = torch.nn.LayerNorm(q_t + v_t) # Layer normalization on the residual
        k_t = torch.nn.LayerNorm(k_t + v_t)

        d1  = torch.einsum('bnhd, bnde -> bnhd', q_t, k_t).contiguous() # Dot product of q_t and k_t (batch_size, num_heads * hidden_dim, seq_length, embed_dim // num_heads)
        d2  = torch.einsum('bhd, de -> bhde', d1, v_t) # Reshape to (batch_size, num_heads * hidden_dim, seq_length, embed_dim // num_heads) and apply linear transformation on the result

        attn_weight = torch.nn.Softmax(dim=-1)
        attn_weight = torch.einsum('bhde, bhde -> bhd', attn_weight, d2) # Dot product of the attention weights (batch_size, num_heads * hidden_dim, seq_length, embed_dim // num_heads) and the dot product output (batch_size, num_heads * hidden_dim, seq_length, embed_dim // num_heads), which are then reshaped to (batch_size, num_heads * hidden_dim, seq_length)
        attn_weight = attn_weight.permute(0, 2, 1, 3).contiguous() # Transpose the dimensions from (batch_size, seq_length, num_heads * hidden_dim, embed_dim // num_heads), and concatenate along the sequence dimension
        if attn_mask is not None:
            attn_weight = attn_weight + attn_mask

        output = torch.einsum('bhd, bhde -> bnhd', attn_weight, v_t) # Reshape to (batch_size, seq_length, num_heads * hidden_dim, embed_dim // num_heads), multiply by the value tensor and reshape back to (batch_size, num_heads * hidden_dim, seq_length, embed_dim // num_heads). The dot product of the scaled attention weights and the value tensor is computed, which are then added to the query tensor

        output = torch.nn.LayerNorm(output + q_t) # Layer normalization on the residual
        return output


# Initializing the model
m = MultiHeadAttention()

# Inputs to the model
q1 = torch.randn(32, 3, 64, 64)
k1 = torch.randn(32, 8, 64, 64)
v1 = torch.randn(32, 8, 64, 64)
attn_mask1 = torch.zeros((1, 64, 64)) # Use the attention mask for each head and sequence dimension to prevent attention to certain positions
