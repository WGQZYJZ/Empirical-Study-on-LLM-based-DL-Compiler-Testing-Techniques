
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale = torch.nn.Parameter(torch.randn(8))
 
    def forward(self, x1, query, key, value):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = torch.randn(8, 8, 5760)
key = torch.randn(8, 8, 5760)
value = torch.randn(1, 2, 5760)
