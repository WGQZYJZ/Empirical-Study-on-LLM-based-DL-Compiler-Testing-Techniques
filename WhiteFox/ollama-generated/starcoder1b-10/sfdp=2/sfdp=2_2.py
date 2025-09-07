
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(64, 32)
        self.v = torch.nn.Linear(32, 8)
        self.dropout = nn.Dropout(p=dropout_p)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, self.qk.weight) # Compute the dot product of the query and the key
        scaled_qk = qk.div(torch.sqrt(torch.tensor([self.scale_factor]).to(m)))  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return self.v(self.dropout(torch.matmul(x1, dropout_qk)))  # Compute the dot product of the dropout output and the value


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
