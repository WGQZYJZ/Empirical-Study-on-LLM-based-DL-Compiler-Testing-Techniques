
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(3, 8)

    def forward(self, query, key, value, scale_factor=0.75):
        qk = self.attn(query, key, value)[0] # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
        output = self.attn(query, dropout_qk, value)[0] # Compute the dot product of the query and key tensors
 
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 8, 32, 64)
key   = torch.randn(1, 32, 16, 32)
value = torch.randn(1, 32, 16, 32)
