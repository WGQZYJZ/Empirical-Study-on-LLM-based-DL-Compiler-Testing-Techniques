
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        kq = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(math.sqrt(float(m.n_heads))) # Compute the dot product of the query and key tensors
        qk = kq.div(math.sqrt(float(m.n_heads))) # Scale the dot product by the inverse scale factor
        softmax_qk = qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        output = qk.matmul(output) + math.sqrt(float(m.n_heads)) * math.sqrt(float(m.head_dim)) * v # Apply linear transformation to the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = Model()


