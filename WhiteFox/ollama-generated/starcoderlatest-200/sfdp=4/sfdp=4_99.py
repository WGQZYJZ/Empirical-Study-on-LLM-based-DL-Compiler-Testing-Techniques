
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, x1, x2, attn_mask=None):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask if attn_mask is not None else qk
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ x2 # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
x2 = torch.randn(2, 16, 64, 64)
attn_mask = torch.ones(3, 3) # The shape of attn_mask should be (batch_size, seq_len, seq_len). Note that the dimension at dim=-2 is the query dimension while the dim=-1 is the key dimension. For example: qk_shape=(8, 64, 64), v_shape=(3, 64, 64) and attn_mask_shape=(3, 64, 64).
