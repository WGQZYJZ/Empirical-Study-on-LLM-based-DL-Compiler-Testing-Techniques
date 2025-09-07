
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=4, key_dim=64)
 
    def forward(self, q1, k1, v1):
        qk = self.attention(q1, k1, v1)[0]  # Apply Multihead Attention to query, key, and value
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)  # Apply softmax on the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(v1)  # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()

# Inputs to the model
q1, k1, v1 = torch.randn(1, 3, 64, 64), torch.randn(2, 3, 64, 64), torch.randn(2, 8, 64, 64)
