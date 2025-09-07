
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, key) # Compute the dot product of the query and key tensors
        scaled_qk = v1 * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax() # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return output.matmul(x2) # Compute the dot product of the dropout output and the value tensor
