
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.einsum('b n c d -> bn c d', (x1, x2)) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(v1 / math.sqrt(x1.size(-1)), dim=-1)  # Apply softmax to the result
        v2 = torch.einsum('bn c d -> b n c', (attn_weight, x2)) # Compute the dot product of the attention weights and the value
        output = v1 * v2
        return output


# Initializing the model
m = Model()

