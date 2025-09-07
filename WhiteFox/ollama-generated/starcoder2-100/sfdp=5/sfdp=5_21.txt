
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Apply batched matrix multiplication to the query and key tensors
        v2  = v1 + attn_mask # Add the attention mask to the scaled dot product result
        v3  = torch.softmax(v2, dim=-1) # Apply softmax to the scaled dot product results
        v4  = torch.dropout(v3, dropout_p, True) # Apply dropout to the softmax output 
        return (v4 @ value).view(query.size()[:-2] + v3.size(-1:])  # Compute the dot product of the dropout output and the value


# Initializing the model
m = Model().eval()


# Inputs to the model
k, q, v = torch.randn((8,50,64)), torch.randn((8,32,64)), torch.randn((8,32,1)) 
