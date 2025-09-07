
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv  = torch.nn.Linear(4, 10)
        self.dense = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        qkv = self.qkv(x1)
        scaled_qkv = qkv.div(torch.sqrt(self.dense.weight))  # Scale the dot product by the inverse of the value diagonal
        softmax_qkv = scaled_qkv.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qkv, p=dropout_p)  # Apply dropout to the softmax output
        y = dropout_qk.matmul(self.dense.weight)  # Compute the dot product of the dropout output and the value
        return y


# Initializing the model
m = Model()


