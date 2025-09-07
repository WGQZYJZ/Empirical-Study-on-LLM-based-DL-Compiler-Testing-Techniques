
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, attn_mask=None):
        qk   = x1 @ self.conv.weight / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        if attn_mask is not None:
            qk  = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        v = self.conv(x1) @ attn_weight  # Compute the weighted sum of the value
        return v
# Initializing the model
m = Model()


