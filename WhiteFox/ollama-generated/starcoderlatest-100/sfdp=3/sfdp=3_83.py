
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
q, k, v, scale_factor, dropout_p = torch.randn(32, 8, 16, 16), \
                                  torch.randn(32, 8, 16, 16), \
                                  torch.randn(32, 8, 16, 16), \
                                  0.5, 0.5
