
class Model(torch.nn.Module):
    def __init__(self, q_size, k_size):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        qk = torch.matmul(x2, x1.transpose(-2, -1))
        scaled_qk = qk.mul(0.1)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v6 = dropout_qk.matmul(x2)
        return v6


# Initializing the model
m  = Model(q_size=16, k_size=8)

# Inputs to the model
inputs = torch.randn(1, 3, 10, 10)
keys = torch.randn(4, 5, 10, 10)
value = torch.randn(4, 5, 64, 64)
