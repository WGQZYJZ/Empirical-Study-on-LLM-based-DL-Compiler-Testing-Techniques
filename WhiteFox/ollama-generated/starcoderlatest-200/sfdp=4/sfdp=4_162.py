
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1, attn_mask=None):
        qk  = self.attn_layer(q1, k1, v1, attn_mask)[0] # Apply the Multihead Attention mechanism on the input tensors
        return qk


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(2, 56, 1, 64)
key = torch.randn(8, 56, 768, 128)
value = torch.randn(8, 56, 768, 128)
attn_mask = torch.zeros([query.size(0), query.size(1), key.size(0), value.size(3)])
