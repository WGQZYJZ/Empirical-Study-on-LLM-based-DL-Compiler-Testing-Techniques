
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        scaled_qk = torch.matmul(v1, v2.transpose(-2, -1)) / math.sqrt(v1.size(-2) * v2.size(-2) + 0.0001)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v2)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
x2 = torch.randn(8, 5, 64, 64)
