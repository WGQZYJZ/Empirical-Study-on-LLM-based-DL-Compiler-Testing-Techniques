
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(10, 32) # Randomly initialize a query matrix with 10 rows and 32 columns
        self.key   = torch.randn(10, 64) # Randomly initialize the key matrix to match it in size with the query matrix above
        self.value = torch.randn(8, 512) # Initialize a value matrix with 8 rows and 512 columns
    def forward(self, p, scale_factor=10):
        inv_scale_factor = float(torch.sqrt(p).reciprocal().sum()) * scale_factor
        qk = torch.matmul(self.query, self.key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=p/50)  # Apply dropout to the softmax output
        output   = dropout_qk.matmul(self.value)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m1  = Model()
__output__1 = m1(torch.randn(256, 80), scale_factor=4.) # Set the scale factor to 3.9 as an example in this case
