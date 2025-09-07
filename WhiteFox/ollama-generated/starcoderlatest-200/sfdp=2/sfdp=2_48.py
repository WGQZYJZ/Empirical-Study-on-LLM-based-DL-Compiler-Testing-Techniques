
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            num_heads=8, 
            embed_dim=512, 
        )
 
    def forward(self, x1, key, query, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = self.attention(query, key, dropout_qk)[0]  # Perform the multihead attention operation and return the final output of the multihead attention operation
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32, 512)
key = torch.randn(1, 32, 512)
query = torch.randn(16, 8, 64, 64)
value = torch.randn(16, 8, 64, 64)
