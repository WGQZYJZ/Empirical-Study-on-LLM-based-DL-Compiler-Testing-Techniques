
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        k1 = torch.matmul(x1, x2.transpose(-2, -1))
        s1 = k1 / math.sqrt(k1.norm(dim=-2, keepdim=True).repeat(1, 8).reshape((x1.size(0), -1)))
        d1 = torch.nn.functional.dropout(s1, p=dropout_p)
 
        v1 = self.conv(x1)
        m1 = torch.matmul(d1, v1)
        return m1

# Initializing the model
m = Model()


