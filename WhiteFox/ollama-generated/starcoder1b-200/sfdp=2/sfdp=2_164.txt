
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of the input tensor with itself (query and key)
        inv_scale_factor = torch.rsqrt(torch.diagonal(qk, dim1=-2, dim2=-1).sqrt() + 1e-10)  # Compute an inverse square root by taking the square root of the diagonal elements along both axes.
        softmax_qk = qk.div(inv_scale_factor)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the input tensor

        return output


# Initializing the model
m = Model()


