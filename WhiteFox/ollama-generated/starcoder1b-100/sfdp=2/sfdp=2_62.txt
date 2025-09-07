
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1  = self.conv(x1)
        v2 = v1  * 0.5
        v3 = v1  * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4  + 1
        v6 = v2  * v5
        qk = torch.matmul(x2, key)  # Compute the dot product of x2 and key
        scaled_qk = qk.div(torch.norm(key))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 32, 32)
