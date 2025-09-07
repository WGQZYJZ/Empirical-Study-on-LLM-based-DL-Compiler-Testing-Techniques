
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.Linear(32, 8)
    
    def forward(self, x1):
        # Initialize the attention weights to zeros and then randomly generate a mask for each element in x1, so that it has the size of x1.
        attn_mask = torch.zeros_like(x1)

        # Compute the query @ key @ value with a dot product
        qkv = self.attn(x1).chunk(3, dim=0)  # Split into three parts: the query part, the key part and the value part
        q = qkv[0]   # Split query part to three tensors
        k = qkv[1]   # Split key part to two tensors
        v = qkv[2]   # Split value part to two tensors

        # Compute the attention weights
        attn_weight = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(k.size(-1)), dim=-1)  # Compute softmax
        attn_weight = attn_weight + attn_mask  # Add the mask to the result

        # Compute the output with weighted sum of value and attention weights
        output = torch.sum(attn_weight * v, dim=1)

        return output


# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
