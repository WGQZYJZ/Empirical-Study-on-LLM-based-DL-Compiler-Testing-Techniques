
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, attn_mask1):  # Apply the above pattern to the first model
        qk = torch.einsum("b h i d, h j d -> b h i j", [query1, key1]) / math.sqrt(
            query1.size(-1)) + attn_mask1
        qk = qk - 0.9
        qk = torch.softmax(qk, dim=-2)
        qk = torch.dropout(qk, 0.5, True) 
        output = torch.einsum("b h i j, h k d -> b h i k", [qk, value1])
        return output

# Initializing the model:
m = Model()

# Input to first model