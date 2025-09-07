
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query = self.conv(x1)  # Compute the output of a pointwise convolution with kernel size 1 to the input tensor x1
        key = torch.matmul(query, x2)  # Compute the dot product of the output of the pointwise convolution and the value
        inv_scale_factor = torch.rsqrt((key ** 2).sum(-1, keepdim=True) + epsilon)
        scale_factor = inv_scale_factor * (self.k / math.sqrt(key.size()[-1]))
        scaled_key = key.div(scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_key = scaled_key.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_key = torch.nn.functional.dropout(softmax_key, p=dropout_p)  # Apply dropout to the softmax output
        value = dropout_key.matmul(x2)  # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model()


