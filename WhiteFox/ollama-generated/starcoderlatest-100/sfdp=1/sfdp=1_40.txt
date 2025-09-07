
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multi_head_attention = torch.nn.MultiHeadAttention()
 
    def forward(self, q, k, v):
        qk = self.multi_head_attention(q, k, value)  # Compute the dot product of query and key tensors with attention
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor with attention
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product with attention
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output with attention
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and value tensor with attention
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 8, 64, 64)
k = torch.randn(1, 8, 64, 64)
v = torch.randn(1, 8, 64, 64)
