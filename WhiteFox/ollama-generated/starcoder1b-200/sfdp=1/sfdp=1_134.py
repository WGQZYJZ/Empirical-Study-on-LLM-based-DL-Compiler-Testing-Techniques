
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, self.key)  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(torch.exp(inv_scale_factor))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(-2)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v1  = self.conv(x1)
        v2 = dropout_qk.matmul(v1)  # Compute the dot product of the dropout output and the value tensor
        v3 = torch.exp(scaled_value) * v2  # Scale and then apply exponentiation to the scaled dot product
        return v3


# Initializing the model
m = Model()


