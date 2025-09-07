
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        attn_weights  = torch.matmul(q1, k1) / math.sqrt(q1.size(-1)) + attn_mask # Compute the attention weights and scale it
        attn_weight = torch.softmax(attn_weights, dim=-1) # Apply softmax to the result
        output = attn_weight @ v1  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

