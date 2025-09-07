
class Attention(torch.nn.Module):
    def __init__(self, dim=8):
        super().__init__()
        self.dim = dim

    def forward(self, x1):
        qk  = torch.matmul(x1, key) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
x1  = torch.randn(8, 32, 64, 64)
attn = Attention()
