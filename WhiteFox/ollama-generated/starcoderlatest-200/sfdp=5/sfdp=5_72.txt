
class AttentionBlock(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.query = torch.nn.Linear(hidden_size * 2, hidden_size) # Create a linear layer with the correct dimensions

    def forward(self, value, key, query, attn_mask=None):
        v1 = torch.cat((value, query), dim=-1) # Combine the two feature maps and concatenate them together
        qk = self.query(v1).view(-1, key.size()[-2], key.size()[-1]) # Apply the linear layer to get a result with shape (batch_size, seq_len, dim)
        
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        
        output = attn_weight @ value # Compute the dot product of the dropout output and the value

        return output

# Initializing the model
m = AttentionBlock(32)

# Inputs to the model
x1 = torch.randn(1, 50, 64)
v1 = torch.randn(1, 2, 64)
k1 = torch.randn(1, 50, 32)
q1 = torch.randn(1, 32, 50)
