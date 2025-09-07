
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, attn_mask):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ v  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(2, 3, 64, 64)
v = torch.randn(2, 3, 64, 64)
attn_mask = torch.zeros((1, 3, 64, 64))
