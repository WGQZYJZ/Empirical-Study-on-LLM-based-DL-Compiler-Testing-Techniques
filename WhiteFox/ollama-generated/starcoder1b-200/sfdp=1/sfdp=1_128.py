
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2) * 0.5
        v2 = v1 * 0.7071067811865476
        qk = torch.matmul(v1, v2) / math.sqrt(scale_factor)
        softmax_qk = F.softmax(qk, dim=-1)
        dropout_qk = nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m  = Model()


