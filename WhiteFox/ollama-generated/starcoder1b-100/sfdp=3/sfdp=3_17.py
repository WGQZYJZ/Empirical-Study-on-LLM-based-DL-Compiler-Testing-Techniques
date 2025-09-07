
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, query, key, value):
        v1 = self.conv(x1)
        vq = torch.matmul(query, key.transpose(-2, -1)) * scale_factor
        vs  = vq.mul(softmax_qk)  # Scale the dot product by a factor
        vd = vd.mul(value)       # Scale the dropout output by a value
        output = dropout_qk.matmul(vd)  # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(1, 2, 8, 8)
key = torch.randn(1, 3, 5, 5)
value = torch.randn(1, 3, 8, 8)
