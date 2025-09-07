
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_linear = torch.nn.Linear(64, 512)
        self.value_linear = torch.nn.Linear(64, 512)
 
    def forward(self, x1, x2):
        query  = self.query_linear(x1)
        value  = self.value_linear(x2)
 
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output
 

# Inputs to the model
x1  = torch.randn(1, 512, 64)
x2  = torch.randn(1, 512, 64)
__output__  = m(x1, x2)

