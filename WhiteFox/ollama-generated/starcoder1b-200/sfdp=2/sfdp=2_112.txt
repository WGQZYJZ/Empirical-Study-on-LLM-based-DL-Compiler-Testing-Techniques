
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 2)
        self.key = torch.nn.Linear(5, 2)
        self.value = torch.nn.Linear(5, 1)
 
    def forward(self, x, y):
        qk = torch.matmul(x, y.transpose(-2, -1)) # Compute the dot product of the query and the key
        inv_scale_factor = torch.rsqrt(torch.diag(qk.mul(qk)))  # Scale the dot product by the inverse scale factor
        softmax_qk = qk / inv_scale_factor  # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return self.value(self.key(dropout_qk))


# Initializing the model
m = Model()


