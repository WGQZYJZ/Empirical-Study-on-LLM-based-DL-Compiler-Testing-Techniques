
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2):
        qk  = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output  = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 32, 64, 64)
x2 = torch.randn(4, 64, 32, 32)
attn_mask = torch.arange((qkv_shape[0] * qkv_shape[1]) // (attn_heads * 2)).unsqueeze(-1).repeat(1, 1, attn_heads, 1).bool()
