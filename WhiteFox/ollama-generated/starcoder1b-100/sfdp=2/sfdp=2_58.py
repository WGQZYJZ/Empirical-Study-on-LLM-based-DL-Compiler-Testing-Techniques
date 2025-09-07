
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(10, 6)
        self.key = torch.nn.Embedding(8, 4)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of x1 and x2
        scaled_qk = qk.div(self.scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v = self.value  # Get the value matrix, for example [0, 0, 0, 0]
        return dropout_qk.matmul(v) # Compute the dot product of the dropout output and the value

# Initializing the model
m = Model()


