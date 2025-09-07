
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, attn_mask):
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = torch.matmul(attn_weight, value)  # Compute the dot product of the attention weights and the value
        return output


# Inputs to the model
query = torch.randn(4, 5, 64, 64)
key = torch.randn(2, 8, 64, 64)
value = torch.randn(3, 5, 128, 128)
attn_mask = torch.eye(attn_mask.shape[0], attn_mask.shape[1]).bool()
