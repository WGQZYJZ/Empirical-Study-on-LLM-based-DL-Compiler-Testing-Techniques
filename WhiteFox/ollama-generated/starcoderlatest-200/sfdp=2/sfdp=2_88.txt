
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv   = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
        self.value_conv = torch.nn.Conv2d(16, 32, 1, stride=1, padding=0)
 
    def forward(self, x):
        q1  = self.query_conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        k1  = self.key_conv   (q1) # Apply pointwise convolution with kernel size 1 to the output of the query conv
        v1  = self.value_conv (k1) # Apply pointwise convolution with kernel size 1 to the output of the key conv
        qk  = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(v1) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
