
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Compute the dot product of the query and key tensors
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        # Scale the dot product by an inverse scale factor to match batch size
        scaled_qk = qk / math.sqrt(self.d_k)  # Scale the dot product by an inverse scale factor to match batch size
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        # Compute the dot product of the dropout output and the value tensor
        output = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()

