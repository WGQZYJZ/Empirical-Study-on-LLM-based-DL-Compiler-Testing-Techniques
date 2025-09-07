
class Model(torch.nn.Module):
    def __init__(self, dim_key, num_heads, attn_mask, hidden_dim, layer_norm):
        super().__init__()
        self.num_heads = num_heads
        self.attn_mask = attn_mask
        self.dropout = torch.nn.Dropout(attn_mask)
 
    def forward(self, qk):
        attn_weight = torch.softmax(qk @ self.key_projection + self.attn_mask, dim=-1)  # Apply softmax to the result of dot product between the query and key plus an attention mask
        attn_weight = self.dropout(attn_weight)  # Apply dropout to the softmax output
        value = torch.matmul(attn_weight, self.value_projection)  # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model(dim_key=8, num_heads=256, attn_mask=0.9, hidden_dim=512, layer_norm=True)

# Inputs to the model
qk  = torch.randn(4, 32, dim_key * num_heads).permute([0, 1, 3, 2])
