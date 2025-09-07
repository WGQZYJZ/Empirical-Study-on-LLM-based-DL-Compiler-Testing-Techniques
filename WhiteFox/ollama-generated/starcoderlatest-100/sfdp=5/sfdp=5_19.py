
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(q1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask  = (k1 == 0).float() # If either key is a padding token
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = torch.matmul(attn_weight, v1)  # Compute the dot product of the dropout output and the value
        return output
# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(2, 3, 64, 64)
k1 = torch.randn(2, 8, 64, 64)
v1 = torch.randn(2, 8, 64, 64)
