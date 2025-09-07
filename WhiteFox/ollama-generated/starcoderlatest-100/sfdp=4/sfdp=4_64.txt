
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention()
 
    def forward(self, q, k, v, attn_mask):
        qk  = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ v # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()
q = torch.randn(16, 3, 8, 8)
k = torch.randn(16, 256, 3, 3) # 16 is the batch size and 256 is the number of heads
v = torch.randn(16, 256, 64, 64) # 16 is the batch size and 256 is the number of heads
attn_mask = torch.ones((16, 8, 8), device=device).bool()

# Inputs to the model
