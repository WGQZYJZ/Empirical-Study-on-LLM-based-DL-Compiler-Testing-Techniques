
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, v1.transpose(-2, -1)) # Compute the dot product of the input and input transpose
        inv_scale_factor = 1.0 / math.sqrt(qk.size()[-1]) # Compute an inverse scale factor
        softmax_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v2 = dropout_qk.matmul(v1) # Compute the dot product of the dropout output and the input tensor
        return v2


# Initializing the model
m = Model()


