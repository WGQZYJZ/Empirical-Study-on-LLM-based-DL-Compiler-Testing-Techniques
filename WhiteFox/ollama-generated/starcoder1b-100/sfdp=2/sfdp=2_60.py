
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool1 = torch.nn.MaxPool2d(kernel_size=(2, 2), stride=(1, 2))
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.pool1(v1)
        v3 = v2  # Note: the second output channel of the max pooling layer is different from the first one
        qk = torch.matmul(x1, self.key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value
        return v3 + output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
v3, __output__  = m(x1)
