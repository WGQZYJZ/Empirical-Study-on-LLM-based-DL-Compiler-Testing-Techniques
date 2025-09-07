
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(
            dim_key=8, dim_value=32, num_heads=4)
 
    def forward(self, x1, x2):
        qk, v, attn_mask = self.attn_layer(x1, x2, x2)  # Compute the scaled dot product of the query and key
        return v


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)  # (batch_size=4, num_head=4, seq_len=8, head_dim=32)
x2 = torch.randn(5, 3, 64, 64)  # (batch_size=5, num_head=5, seq_len=12, head_dim=32)
