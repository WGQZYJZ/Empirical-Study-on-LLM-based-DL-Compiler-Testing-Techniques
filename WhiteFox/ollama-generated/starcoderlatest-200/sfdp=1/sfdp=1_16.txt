
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn((3, 8, 4, 4)))
 
    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2) # Compute the dot product of a query tensor and a key tensor
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(x3) # Compute the dot product of the dropout output and a value tensor
        return output


# Inputs to the model
x1 = torch.randn(2, 3, 4, 4) # query
x2 = torch.randn(2, 8, 4, 4) # key
x3 = torch.randn(2, 8, 64, 64) # value
