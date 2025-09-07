
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(384, 10)
        self.key = torch.nn.Linear(10, 20)
        self.value = torch.nn.Linear(20, 20)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        y   = dropout_qk.matmul(y2)  # Compute the dot product of the dropout output and the value tensor
        return y


# Initializing the model
m = Model()


