
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        kq = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        kq = kq.mul(scale_factor)              # Scale the dot product by a factor
        softmax_qk = kq.softmax(dim=-1)       # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        out = dropout_qk.matmul(v6)  # Compute the dot product of the dropout output and the value tensor
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
