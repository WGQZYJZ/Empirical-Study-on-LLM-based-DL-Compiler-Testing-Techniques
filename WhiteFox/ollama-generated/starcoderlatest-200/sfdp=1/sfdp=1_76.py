
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)

    def forward(self, query, key, value, scaled_qk, softmax_qk, dropout_qk, output):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output     = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return qk, scaled_qk, softmax_qk, dropout_qk, output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key, value = torch.rand_like(x1), torch.rand_like(x1)
__output__, scaled_qk, softmax_qk, dropout_qk, output = m(x1, key, value)


