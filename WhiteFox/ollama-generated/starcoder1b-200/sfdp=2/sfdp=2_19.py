
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) # Compute the dot product of x1 and x1.
        inv_scale_factor = torch.rsqrt(torch.clamp(qk + self.eps, min=self.eps) + self.eps) # Scale the dot product by the inverse scale factor.
        softmax_qk = qk / inv_scale_factor  # Apply softmax to the scaled dot product.
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output.
        output = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and the value.
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
