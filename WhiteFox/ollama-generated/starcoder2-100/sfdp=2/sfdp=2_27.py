

class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0., inv_scale_factor=1.):
        v = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key 
        v = v / inv_scale_factor
        v = v.softmax(dim=-1)
        
        if dropout_p > 0:
            v = torch.nn.functional.dropout(v, p=dropout_p)  # Apply dropout to the softmax output
 
        return value @ v  # Compute the dot product of the dropout output and a value


# Initializing the model
model = Attention()

