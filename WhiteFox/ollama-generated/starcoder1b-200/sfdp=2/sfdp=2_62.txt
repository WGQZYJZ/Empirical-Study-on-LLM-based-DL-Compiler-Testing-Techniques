
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(20, 4)
        self.key   = torch.nn.Linear(15, 4)
        self.value = torch.nn.Linear(8, 4)
        self.scale = 1 / (np.sqrt(self.key_dim))
 
    def forward(self, x):
        q = self.query(x)
        k = self.key(x)
        v = self.value(x)
        qk = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(self.scale) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        out = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value
        return out


# Initializing the model
m = Model()


