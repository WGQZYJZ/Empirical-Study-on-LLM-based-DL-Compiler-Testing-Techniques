
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_q = torch.nn.Linear(8, 8) 
        self.attn_k = torch.nn.Linear(8, 8) 
        self.attn_v = torch.nn.Linear(8, 8)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, self.attn_q.weight.transpose(-2, -1)) # Compute the dot product of the query and key, and scale it
        qk = qk + x2 # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = torch.matmul(attn_weight, self.attn_v.weight.transpose(-2, -1)) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8) # Query tensor
x2 = torch.randn(1, 8) # Key tensor
