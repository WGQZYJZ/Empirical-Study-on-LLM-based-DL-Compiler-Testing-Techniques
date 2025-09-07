
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = self.attention(dropout_qk, key, value)[0]  # Use MultiheadAttention() to compute the attention output
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 32, 128)
key   = torch.randn(16, 64, 128)
value = torch.randn(16, 64, 512)
