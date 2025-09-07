
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1) # (B x C x T x T)
        self.conv2 = torch.nn.Conv2d(64, 64, 7, stride=5, padding=0) # (B x C x N x N)

    def forward(self, query, key, attn_mask):
        v1 = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))  # Apply a matrix multiply to compute the dot product of the query and key tensors
        v2 = self.conv1(attn_mask) # Reshape the attention mask
        attn_weight = torch.softmax(v1 + v2, dim=-1) # Add the scaled dot-product attention scores to the attention mask, then apply softmax
        v3  = torch.matmul(attn_weight, value) # Compute the dot product of the attention weights and the value
        return self.conv2(v3) # Apply a convolution with kernel size 7x7 to compute the output tensor


# Inputs to the model
query = torch.randn(1, 8, 64, 64)
key = torch.randn(1, 8, 64, 64)
attn_mask = torch.randn(1, 8, 64, 64)
