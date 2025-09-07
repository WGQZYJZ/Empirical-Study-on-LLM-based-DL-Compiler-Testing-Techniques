
class Attention(torch.nn.Module):
    def __init__(self, num_attention_heads):
        super().__init__()
        self.qkv = torch.nn.Linear(32, 48)
 
    def forward(self, x1):
        qk = self.qkv(x1).chunk(num_attention_heads * 3, dim=0)
        output = torch.einsum("bhqd,bjhd->bhqj", [qk[0], qk[2]])
        return output
 
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads):
        super().__init__()
        self.attention  = Attention(num_attention_heads)
 
    def forward(self, x1, x2):
        # Apply the attention to the two inputs.
        output = self.attention(x1).div(np.sqrt(4)) + self.attention(x2)
        return output


# Initializing the model with 8 attention heads
m  = Model(num_attention_heads=8)

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
x2 = torch.randn(1, 32, 64, 64)
