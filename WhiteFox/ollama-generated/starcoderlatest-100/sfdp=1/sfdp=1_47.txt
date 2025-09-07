
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, key, query, scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(scale_factor)  # Scale the dot product by the scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output
# Initializing the model
m = Model()
scale_factor = torch.tensor([128])
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(256, 3, 64, 64)
key = torch.randn(256, 3, 64, 64)
query = torch.randn(1, 8, 64, 64)
