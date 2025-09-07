
class Model(torch.nn.Module):
    def __init__(self, input_dim, num_heads, output_dim):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=input_dim, 
            num_heads=num_heads, 
        )
 
    def forward(self, q1, k1, v1):
        (attn_output, attn_weight) = self.attn(q1, k1, v1)  # Compute the attention
        return attn_output

# Initializing the model
m = Model(512, 8, 64)

# Inputs to the model
x1 = torch.randn(3, 512, 64, 64)
k1 = torch.randn(3, 512, 64, 64)
v1 = torch.randn(3, 512, 64, 64)
