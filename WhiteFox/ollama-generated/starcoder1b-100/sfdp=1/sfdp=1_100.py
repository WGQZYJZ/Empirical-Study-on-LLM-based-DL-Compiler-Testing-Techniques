
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 2)
        self.key = torch.nn.Linear(5, 3)
        self.value = torch.nn.Linear(8, 9)
        self.layer_norm = torch.nn.LayerNorm([10, 3, 6])
 
    def forward(self, x):
        qk = self.query(x) # Compute the query tensor from its input dimension `10`
        k = self.key(x)  # Compute the key tensor from its input dimension `5`
        v = self.value(x)  # Compute the value tensor from its input dimension `8`
        qk = qk.contiguous().view(qk.size(0), -1, qk.size(-2), k.size(-2))
        scaled_qk = qk.div(self.layer_norm(qk)**-0.5) # Scale the dot product by its inverse scale factor and store in a variable `scaled_qk`
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return dropout_qk.matmul(v).contiguous().view(x.size(0), -1) # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(2, 5, 10)
