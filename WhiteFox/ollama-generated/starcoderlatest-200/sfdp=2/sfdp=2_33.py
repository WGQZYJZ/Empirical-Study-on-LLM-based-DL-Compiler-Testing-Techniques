
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk):
        softmax_qk = qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output


# Inputs to the model
qk = torch.randn(1, 64, 8, 64)
