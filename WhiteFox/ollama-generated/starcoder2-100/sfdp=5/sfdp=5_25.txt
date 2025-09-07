
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k2, v3):
        v4  = (q1 @ k2.transpose(-2, -1)) / math.sqrt(query_size) + attn_mask
        v5  = torch.softmax(v4, dim=-1) # Compute the softmax of the scaled dot product of query and key
        v6  = torch.dropout(v5, dropout_p=0.1, training=True) # Apply dropout to the softmax output
        v7  = v3 @ v2  # Compute the dot product of the value matrix and the dropout output
        return v7

# Initializing the model
m = Model()

