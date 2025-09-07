
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 1024)
 
    def forward(self, x1):
        v1  = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.size(-1)) # Compute the dot product of the query and key, and scale it
        v2  = v1 + torch.matmul(torch.ones_like(v1), self.attn_mask) # Add the attention mask to the scaled dot product
        v3  = torch.softmax(v2, dim=-1) # Apply softmax to the result
        v4  = torch.dropout(v3, dropout_p, True) # Apply dropout to the softmax output
        v5  = self.attn_weight @ self.value # Compute the dot product of the dropout output and the value
        return v6

# Initializing the model
m = Model()


class Test(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = self.model(x1)
        return x2
 

test = Test()
out = test(x1)
 