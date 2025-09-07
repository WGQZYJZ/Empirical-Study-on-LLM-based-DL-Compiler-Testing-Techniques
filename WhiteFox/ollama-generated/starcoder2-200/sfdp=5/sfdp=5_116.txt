
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, query2, key2, value2):
 
        vq1  = query1 @ key1.transpose(-2, -1) / math.sqrt(query1.size(-1)) # Compute the dot product of the query and key
        vq1  = vq1 + attn_mask1  # Add the attention mask to the scaled dot product
        vaw1 = torch.softmax(vq1, dim=-1)  # Apply softmax to the result
        
        vaw1 = torch.dropout(vaw1, dropout_p, True)  # Apply dropout to the softmax output
        vo1   = vaw @ value  # Compute the dot product of the dropout output and the value

        vq2  = query2 @ key2.transpose(-2, -1) / math.sqrt(query2.size(-1))# Compute the dot product of the query and key
        vq2  = vq2 + attn_mask2 # Add the attention mask to the scaled dot product
        vaw2 = torch.softmax(vq2, dim=-1) # Apply softmax to the result
        
        vaw2 = torch.dropout(vaw2, dropout_p, True) # Apply dropout to the softmax output
        vo2   = vaw @ value  # Compute the dot product of the dropout output and the value

        return (vo1 + vo2) / math.sqrt(query1.size(-1))

# Initializing the model
m = Model()

