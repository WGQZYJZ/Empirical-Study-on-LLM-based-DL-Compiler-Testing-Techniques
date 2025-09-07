
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, k1, v):
        v1 = self.conv(x1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5  # Multiply the output of the convolution by 0.5
        v3 = v1 * 0.7071067811865476  # Multiply the output of the convolution by 0.7071067811865476
        qk = torch.matmul(v2, k1)  # Compute the dot product of v2 and k1
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(v3)  # Compute the dot product of the dropout output and v3
        return output


# Initializing the model
m = Model()


