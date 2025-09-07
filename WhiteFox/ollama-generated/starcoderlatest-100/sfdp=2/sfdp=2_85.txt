
class AttentionModel(torch.nn.Module):
    def __init__(self, n_heads):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(embed_dim=8, num_heads=n_heads)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        attention = self.att(query, dropout_qk, value)[0] # Compute the output of multi-head attention
        return attention


# Initializing the model
m = AttentionModel(n_heads=8)

# Inputs to the model
x1 = torch.randn(32, 64, 7, 7)
