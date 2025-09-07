
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=8, num_heads=1)
 
    def forward(self, query, key, value, mask=None):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        attn_output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        attn_output = attn_output * self.scale_factor  # Scale the attention result by a factor
        return attn_output, softmax_qk


# Inputs to the model
x1 = torch.randn(1, 32, 64)
__output__, __softmax_qk__ = m(query=x1, key=None, value=None, mask=None)