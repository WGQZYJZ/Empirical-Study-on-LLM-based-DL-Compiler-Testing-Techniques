
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, scaled_qk, softmax_qk, dropout_qk, output):
        return self.matmul(query, key)  # Compute the dot product of the query and the key


# Initializing the model
m = Model()

# Query to the model
qk  = torch.randn(1024, 3072)

# Scaled query from the model
scaled_qk = qk / math.sqrt(256.0)

# Softmax output from the model
softmax_qk  = scaled_qk.softmax(dim=-1)

# Dropped-out softmax output from the model
dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

# Output from the model
output = dropout_qk.matmul(value)
