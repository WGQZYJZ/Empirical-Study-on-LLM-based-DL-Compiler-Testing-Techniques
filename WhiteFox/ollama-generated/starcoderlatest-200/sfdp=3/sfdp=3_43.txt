
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(512, 512)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 32, 512, 64)  # Batch size is 1 for simplicity, in real applications this should be 1, but it is easy to get confused if not
key   = torch.randn(32, 512, 2048, 64)
value = torch.randn(32, 512, 2048, 64)
scale_factor = torch.ones((32,)) * (1 / math.sqrt(float(512)))
dropout_p    = 0.1
