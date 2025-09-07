
class Model(torch.nn.Module):
    def __init__(self, num_heads=8, dim_k=16):
        super().__init__()
        self.head = torch.nn.Linear(dim_k, dim_k)
        self.scale = math.sqrt(dim_k)
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, x1, x2):
        # Compute the dot product of the query and the key
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and the key
        # Scale the dot product by the inverse scale factor
        scaled_qk = qk.div(self.scale)
        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)
        # Apply dropout to the softmax output
        dropout_qk = self.dropout(softmax_qk)  # Apply dropout to the softmax output
        # Compute the dot product of the dropout output and a value
        output = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, 64, 128)
k1 = torch.randn(1, 128, 128)
