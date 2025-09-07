
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Apply pointwise convolution with kernel size 1 to the input tensor
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v = self.conv(qk)  # Apply pointwise convolution
        scaled_v = v.mul(scale_factor)  # Scale the dot product by a factor
        softmax_v = scaled_v.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_v = torch.nn.functional.dropout(softmax_v, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_v.matmul(value)


# Initializing the model
m = Model()


