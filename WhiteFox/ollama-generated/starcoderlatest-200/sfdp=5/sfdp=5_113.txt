
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(2048, 2048)
 
    def forward(self, q1, k1, v1, attn_mask):
        qk = q1 @ k1.transpose(-2, -1) / math.sqrt(q1.size(-1))  # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        return attn_weight @ v1


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(8, 3072, 64, 64)
k1 = torch.randn(8, 3072, 64, 64)
v1 = torch.randn(8, 3072, 64, 64)
attn_mask = torch.rand((8, 1, 64, 64)) > dropout_p  # Generate an attention mask with random entries that are greater than the dropout probability
