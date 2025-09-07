
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, x1.transpose(-2, -1)) / float(self.scale_factor)  # Compute the dot product of two matrices using dot products and element-wise division operations with inbuilt math ops
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and a value tensor
        return v

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
