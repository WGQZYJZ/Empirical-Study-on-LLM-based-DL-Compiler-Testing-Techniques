
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, q1, k1, v1):
        attn_out  = self.attn(q1, k1, v1)[0] # Compute the output of the attention layer
        return attn_out

# Initializing the model
m  = Model()


# Inputs to the model:
q1   = torch.randn(2, 3, 8) # The query tensor with shape [2, 3, 8]
k1   = torch.randn(4, 3, 8) # The key tensor with shape [4, 3, 8]
v1   = torch.randn(5, 4, 8) # The value tensor with shape [5, 4, 8]


