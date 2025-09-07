
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(4, 8)
 
    def forward(self, qk, k, v, attn_mask):
        v  = torch.nn.functional.softmax(qk @ k.transpose(-2, -1), dim=-1) * v # Compute the scaled dot-product of query and key
        v = v + attn_mask # Add attention mask to the scaled dot-product
        output = self.attn(qk, k, v, mask=attn_mask)[0]  # Get the result
        return output


# Inputs to the model
query = torch.randn(1, 4, 8)
key   = torch.randn(1, 8)
value = torch.randn(1, 256, dtype=torch.float32)
attn_mask = value > 0 # This mask is used to remove non-significant values in the output
