
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2, attn_mask):
        qk  = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ x2 # Compute the dot product of the attention weights and the value
        return output


# Inputs to the model
x1 = torch.randn(16, 32, 784)
x2 = torch.randn(16, 512, 784)
attn_mask = torch.randint(0, 2, (16, 1))
