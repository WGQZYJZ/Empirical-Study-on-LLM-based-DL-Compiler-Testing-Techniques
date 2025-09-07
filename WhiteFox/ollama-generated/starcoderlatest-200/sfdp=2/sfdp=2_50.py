
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(embed_dim=16, num_heads=2)
 
    def forward(self, q, k, v, x, inv_scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(16, 32, 10, 48)
k = torch.randn(32, 32, 56, 96)
v = torch.randn(32, 32, 56, 96)
x = torch.randn(32, 16, 4, 108)
inv_scale_factor = 1/sqrt(3)
dropout_p = 0.2
