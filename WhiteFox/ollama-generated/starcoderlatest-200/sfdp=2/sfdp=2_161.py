
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value):
        v1, attn_weights = self.attn(query, key, value)
        return v1, attn_weights


# Initializing the model
m = Model()

 # Inputs to the model
q1 = torch.randn(3, 64, 64)
k1 = torch.randn(3, 64, 64)
v1 = torch.randn(3, 64, 64)
__output__, __attn_weights__ = m(q1, k1, v1)

 # The output of the attention mechanism is used as the input to a linear transformation
#   to obtain the context vector
__context_vector__ = torch.matmul(__attn_weights__, v1)

 # This context vector is then used in the next layer to compute the output
 