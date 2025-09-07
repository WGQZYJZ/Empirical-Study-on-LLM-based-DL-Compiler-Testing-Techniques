
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1, attn_mask1):
        k1  = k1.transpose(-2, -1) # Transpose key and query for attention
        output1, _, _ = self.attn(q1, k1, v1, attn_mask=attn_mask1)
        return output1


# Initializing the model
m = Model()


# Inputs to the model
k1 = torch.randn(8, 64, 32, 32)
q1 = torch.randn(8, 64, 32, 32)
v1 = torch.randn(8, 64, 64, 64)
attn_mask1 = torch.ones(1, 1, 64, 64).bool()


# Output
