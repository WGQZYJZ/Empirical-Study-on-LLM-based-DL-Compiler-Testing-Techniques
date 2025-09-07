
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 64)
 
    def forward(self, x1, x2):
        q1 = self.query(x1)
        q2 = self.query(x2)
        k1 = self.key(x1)
        k2 = self.key(x2)
        v1 = self.value(x1)
        v2 = self.value(x2)
 
        attn_weight  = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(k1.size(-1)) # Compute the dot product of query and key, and scale it
        attn_weight += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(attn_weight, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
 
        output = torch.matmul(attn_weight, v2)  # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
