
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.query(x1)
        qk = torch.matmul(v1, x2.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v2 = torch.matmul(dropout_qk, x2) # Compute the dot product of the dropout output and the value
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64) # A query with a batch size of 3, channels of 64, and height and width of 64 pixels
x2 = torch.randn(3, 64, 64) # A key with the same shape as x1 but with a batch size of 3


# Outputs to check against:
