
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 512)
        self.key = torch.nn.Linear(768, 512)
 
    def forward(self, x1):
        qk = torch.matmul(self.query(x1), self.key.transpose(-2, -1)) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + 10 # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = torch.matmul(attn_weight, self.value(x1)) # Compute the dot product of the dropout output and the value
        return output

# Inputs to the model
x1 = torch.randn(1, 768, 2049)
