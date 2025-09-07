
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.Linear(4, 2)
 
    def forward(self, v1, k1, qk1):
        # Compute the softmax of the scaled dot-product attention weights.
        attn_weights  = torch.softmax(qk1, dim=-1)
        attn_mask = attn_weights > 0  # Compute a binary mask for invalid values in the attention weight tensor
        # Compute the dot product of the value and key.
        output = v1 @ k1.transpose(-2, -1) / math.sqrt(v1.size(-1))
        # Apply the softmax to get the attention weights.
        attn_weights = torch.softmax(output, dim=-1)
        # Apply masking with `0` to the attention weight tensor and sum it up using the broadcasting rules.
        output = (attn_mask * attn_weights).sum(-2)
        return output


# Initializing the model
a = Attention()

# Inputs to the model
v1  = torch.randn(4, 6, 32, 32)
k1  = torch.randn(4, 8, 32, 32)
qk1 = v1 @ k1.transpose(-2, -1) / math.sqrt(v1.size(-1)) # Compute the dot product of the value and key.
