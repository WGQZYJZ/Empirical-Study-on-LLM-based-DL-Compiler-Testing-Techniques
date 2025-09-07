
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w_k = torch.nn.Linear(10, 256)
 
    def forward(self, q, k):
        qk = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output

# Inputs to the model
q1, k1 = torch.randn(80, 64), torch.randn(80, 256)
