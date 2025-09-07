
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, x):
        _, scaled_qk, attn = self.attention(q=x, k=x, v=x)  # Compute the attention matrix
        softmax_qk = scaled_qk / torch.sqrt(attn.shape[-1])  # Apply softmax to the scaled dot product
        output = softmax_qk.matmul(v)  # Multiply the softmax output by the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(4, 512, 2048, 3072)
