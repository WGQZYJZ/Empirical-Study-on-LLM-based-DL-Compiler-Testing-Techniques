
class Model(torch.nn.Module):
    def __init__(self, n = 512, qk = None):
        super().__init__()
 
    def forward(self, xq, k, v):
        qk = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result 
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m  = Model()


# Inputs to the model
xq = torch.randn(16, n) # Input query tensor of shape (batch size, number of heads * hidden dimension in each head).
k = torch.randn(512*8,n//8) # Key tensor of shape (number of heads * hidden dimension in each head, batch_size) 
v = torch.randn(512*8, n//8) # Value tensor of shape (number of heads * hidden dimension in each head ,batch size).
attn_mask = torch.zeros([n]) # Attention mask.
