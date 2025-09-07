
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        q2, k2, v2 = self.attn_layer(q1, k1, v1)
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(32, 8, 768)  # The query tensor
k1 = torch.randn(8, 32, 768)  # The key tensor
v1 = torch.randn(32, 8, 768)  # The value tensor
