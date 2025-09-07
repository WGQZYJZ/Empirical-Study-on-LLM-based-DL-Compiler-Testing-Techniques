
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._input1 = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = MyModel()
 
# Inputs to the model
x = torch.randn(2, 3, 10)
k = torch.randn(4, 5)
v = torch.randn(7,)
attn_mask = -torch.ones((6, 8), dtype=torch.float) / float("inf")
attn_mask[np.diag_indices_from(attn_mask)] = 0
 
# Model outputs on different inputs x, k and v to m(x,k,v).
out1  = m(x, k, v)

out2 = MyModel()(x)