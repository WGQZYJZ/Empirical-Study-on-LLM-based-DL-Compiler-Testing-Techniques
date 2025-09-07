
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_linear = torch.nn.Linear(512, 512)
        self.k_linear = torch.nn.Linear(512, 512)
        self.v_linear = torch.nn.Linear(512, 512)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / math.sqrt(key.shape[-1]) # Scale the dot product by the square root of the number of attention heads
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(2, 512, 1024)
key = torch.randn(2, 512, 1024)
value = torch.randn(2, 512, 16)
