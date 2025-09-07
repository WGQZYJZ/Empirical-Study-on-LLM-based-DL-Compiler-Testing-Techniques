
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1) # Pointwise convolution with kernel size 1 for query tensor 
        self.key   = torch.nn.Conv2d(3, 8, 1) # Pointwise convolution with kernel size 1 for key tensor 

    def forward(self, x1):
        qk = torch.matmul(self.query(x1), self.key(x1).transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk * self.value(x1) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
