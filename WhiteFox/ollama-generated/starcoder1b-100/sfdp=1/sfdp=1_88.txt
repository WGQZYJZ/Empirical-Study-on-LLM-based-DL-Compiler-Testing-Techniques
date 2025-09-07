
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x2.transpose(-2, -1)) * 0.5
        v3 = torch.matmul(v1, x2.transpose(-2, -1)) * 0.7071067811865476
        v4 = torch.erf(v3) + 1
        v5 = v2 * v4
        dropout_qk = torch.nn.functional.dropout(v5, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1  = torch.randn(3, 64, 64)
k1 = torch.randn(8, 3, 64, 64)
