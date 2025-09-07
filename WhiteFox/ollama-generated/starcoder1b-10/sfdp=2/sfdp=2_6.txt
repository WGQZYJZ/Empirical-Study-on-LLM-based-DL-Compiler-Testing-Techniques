
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(float(kernel_size[0]) * float(kernel_size[1])) # Compute the dot product of the query and the key
        scaled_qk = qk / math.sqrt(float(kernel_size[0]) * float(kernel_size[1]))  # Scale the dot product by the inverse scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(x3)  # Compute the dot product of the dropout output and the value


# Initializing the model
m = Model()


