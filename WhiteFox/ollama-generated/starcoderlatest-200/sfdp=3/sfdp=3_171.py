
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        scaled_qk = self.attention(query, key, value, attn_mask=None).float() # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor

# Initializing the model
m = Model()


