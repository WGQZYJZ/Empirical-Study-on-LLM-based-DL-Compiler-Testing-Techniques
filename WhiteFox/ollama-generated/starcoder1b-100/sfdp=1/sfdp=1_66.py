
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(float(n_q_kv + epsilon))  # Compute the dot product of the query and key tensors and divide by sqrt(float(n_q_kv + epsilon)).
        scaled_qk = qk.div(math.sqrt(float(n_q_kv)))  # Scale the dot product by the inverse scale factor.
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product.
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output.
        x2 = dropout_qk.matmul(x1)  # Compute the dot product of the dropout output and the value tensor.
        return x2


# Initializing the model
m = Model()


