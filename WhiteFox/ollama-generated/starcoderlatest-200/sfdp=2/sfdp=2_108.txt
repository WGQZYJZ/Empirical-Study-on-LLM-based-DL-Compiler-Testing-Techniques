
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=128, num_heads=6)
 
    def forward(self, query, key, value):
        qk = self.attention(query, key, value)[0] # Compute the dot product of the query and the key
        scaled_qk = qk / 3  # Scale the dot product by 3
        softmax_qk = scaled_qk.softmax(-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
        output = self.attention(dropout_qk, value, value)[0]  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
query = torch.randn(4, 128, 7, 7)
key = torch.randn(4, 64, 5, 5)
value = torch.randn(4, 64, 5, 5)


# Inputs to the model
