
class Model(torch.nn.Module):
    def __init__(self, n_heads=4):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=128, num_heads=n_heads)
 
    def forward(self, x, x_pos):
        qk  = torch.matmul(x, x.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk / math.sqrt(x_pos.size(-1)) # Scale the dot product by 1/sqrt(attention size)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        attention  = self.attention(x, x_pos, dropout_qk)[0] # Compute the dot product of the attention weights and key values 
        attention += x # Add key values for attention
        return attention


# Inputs to the model
x1 = torch.randn(8, 32, 4)
x2 = torch.randn(8, 32, 4)
