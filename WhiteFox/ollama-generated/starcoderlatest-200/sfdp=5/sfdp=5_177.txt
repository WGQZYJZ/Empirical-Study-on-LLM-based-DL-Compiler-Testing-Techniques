
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2, attn_mask):
        qk = self.attn(x1, x2, x2)[0] # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        return self.attn(x1, x2, x2)[0] @ value
# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(8, 3, 64, 64) # Input of shape (num_heads, num_attention_heads, input_len, key_len)
x2 = torch.randn(8, 3, 64, 64) # Input of shape (num_heads, num_attention_heads, query_len, value_len)
attn_mask = torch.rand(8, 1, 64, 64).bool() # Attention mask with shape (num_heads, num_attention_heads, key_len, key_len)
