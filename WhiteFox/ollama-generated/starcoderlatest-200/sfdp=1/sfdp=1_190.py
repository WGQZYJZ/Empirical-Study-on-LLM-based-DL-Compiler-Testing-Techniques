
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, qk):
        v6 = self.conv(x1)
        softmax_qk = qk.softmax(dim=-1)
        output = torch.matmul(softmax_qk, value)
        return output
 
