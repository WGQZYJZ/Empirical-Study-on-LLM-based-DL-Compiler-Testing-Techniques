
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key):
        v1 = self.query(query)
        v2 = self.key(key)
        v3 = torch.matmul(v1, v2.transpose(-2, -1)) * (0.5 / 0.7071067811865476)
        softmax_qk = torch.softmax(v3, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=0.5)
        output = torch.matmul(dropout_qk, v2)
        return output
