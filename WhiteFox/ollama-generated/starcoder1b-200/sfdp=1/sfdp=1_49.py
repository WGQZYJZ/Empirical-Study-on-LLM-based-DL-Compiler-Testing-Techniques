
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
        qk = torch.matmul(query, key.transpose(-2, -1))
        k_scaled = qk.div(inv_scale_factor)
        v_scaled = value.div(inv_scale_factor)
        softmax_qk = k_scaled.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v_scaled)
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
