
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5

        qk = torch.matmul(v2, v2.transpose(-2, -1)) # compute the dot product of two vectors (the query and the key).
        inv_scale_factor = 1 / 64.0
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by a scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25) # Apply dropout to the softmax output

        v4 = self.conv(x2)
        output = dropout_qk.matmul(v4) # compute the dot product of a vector and the output of another convolution

        return output


# Initializing the model
m = Model()

