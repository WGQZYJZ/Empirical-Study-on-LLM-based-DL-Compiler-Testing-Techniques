
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, v1.transpose(-2, -1))
        v2 = v1 * inv_scale_factor
        w_softmax_qk = w_softmax_q.softmax(dim=-1)
        v3 = dropout_w.dropout(w_softmax_qk, p=dropout_p)
        v4 = v3 * x1
        return v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
