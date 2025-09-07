
class Model(torch.nn.Module):
    def __init__(self, d_model=512, num_heads=8):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, 3 * num_heads * d_model)
 
    def forward(self, x1):
        batch_size, _, sequence_length, _ = x1.shape
        qk = self.qkv(x1).view(batch_size, -1, 3, num_heads, sequence_length).permute(0, 2, 3, 1, 4)
        attn_weights = torch.softmax(qk[-1], dim=-2) # Apply softmax to the result of the last linear layer for each query in the batch
        attn_weights = torch.dropout(attn_weights, dropout_p, True) # Apply dropout to the attention weights before feeding it into the value layer
        values = torch.einsum('bijhql,bjhqk->bkhq', attn_weights, x1).permute(0, 3, 2, 1, 4) # Compute the dot product of each query and its respective value
        return values


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
