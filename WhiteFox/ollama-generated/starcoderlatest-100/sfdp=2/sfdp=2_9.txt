
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(num_heads=8, input_dim=32)
 
    def forward(self, q1, k1, v1):
        # Attention Layer
        attn_output = self.attention_layer(q1, k1, v1)[0]
        return attn_output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(16, 32, 128)
y1 = torch.randn(16, 8, 64)
