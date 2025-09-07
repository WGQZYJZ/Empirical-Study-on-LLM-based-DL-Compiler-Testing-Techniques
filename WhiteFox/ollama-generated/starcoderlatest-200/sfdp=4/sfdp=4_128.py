
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 3)
 
    def forward(self, q1, k1, v1):
        # Compute the attention weights for each head with softmax (per query and key). 
        v_wts, attn_weight = self.attention(q1, k1, v1)
 
        return v_wts * attn_weight
 
 
# Initializing the model
m = Model()

 # Inputs to the model
 q1 = torch.randn(1, 8, 64, 64)
 k1 = torch.randn(1, 8, 64, 64)
 v1 = torch.randn(1, 8, 64, 64)

 