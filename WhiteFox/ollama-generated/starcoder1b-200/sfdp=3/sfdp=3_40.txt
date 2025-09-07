
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 4)
        self.key = torch.nn.Embedding(10, 8)

    def forward(self, x1, x2):
        qk = self.query(x1).matmul(self.key) # Compute the dot product of query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and value tensor
        return output


# Initializing the model
m  = Model()

