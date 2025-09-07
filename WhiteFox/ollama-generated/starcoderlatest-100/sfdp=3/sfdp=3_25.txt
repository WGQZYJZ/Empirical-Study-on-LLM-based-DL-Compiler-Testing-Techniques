
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(p=dropout_p)
 
    def forward(self, qk, v):
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
        return output
 
