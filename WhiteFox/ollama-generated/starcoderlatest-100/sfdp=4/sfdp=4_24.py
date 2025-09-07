
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 3)
        self.key   = torch.nn.Linear(128, 3)
 
    def forward(self, qk_input, value_input):
        q  = self.query(qk_input)
        k  = self.key(qk_input)
        v  = self.value(qk_input)
 
        qk = torch.einsum('b i j d -> b j i d', [q, k]) / math.sqrt(q.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)  # Apply softmax to the result
        output      = torch.einsum('b j i d -> b i d', [attn_weight, v])
        return output


# Initializing the model
m = Model()


# Inputs to the model
qk_input   = torch.randn(1, 3, 64, 64)
value_input = torch.randn(1, 3, 64, 64)
__output__  = m(qk_input, value_input)

