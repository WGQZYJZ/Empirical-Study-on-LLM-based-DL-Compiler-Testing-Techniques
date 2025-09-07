
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.value_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        q = self.query_conv(x1)
        k = self.key_conv(x2)
        v = self.value_conv(x2)
        k  = k.transpose(-2, -1)  # Transpose the key to get an input of the same shape as key_value
        scaled_k = torch.bmm(q, k) / math.sqrt(float(self.scale))  # Scale the dot product by the inverse scale factor
        softmax_k = scaled_k.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_k = torch.nn.functional.dropout(softmax_k, p=dropout_p)  # Apply dropout to the softmax output
        x3 = dropout_k.matmul(v)  # Compute the dot product of the dropout output and the value
        return x3


# Initializing the model
m = Model()


