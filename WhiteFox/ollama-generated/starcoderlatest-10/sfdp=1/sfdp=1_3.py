
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.layer_norm = torch.nn.LayerNorm([64, 64], eps=1e-5)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v1 = self.layer_norm(v1)
        v2 = self.conv(x2)
        v2 = self.layer_norm(v2)
        qk = torch.matmul(v1, v2.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v2)
        return v6

