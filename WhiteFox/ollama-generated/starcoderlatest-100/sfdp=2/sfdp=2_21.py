
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, q1, k1, v1):
        v1 = self.conv(v1)
        scaled_qk = torch.matmul(q1, k1.transpose(-2, -1)) / scale_factor 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(32, 64, 56, 56)
k1 = torch.randn(32, 64, 19, 19)
v1 = torch.randn(32, 8, 13, 13)
