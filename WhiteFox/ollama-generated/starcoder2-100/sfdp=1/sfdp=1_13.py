
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(3072, 8192)
 
    def forward(self, xq, kq, vk):
        v1 = torch.matmul(xq, kq.transpose(-2, -1))
        v2 = v1 / math.sqrt(8192.0)
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.5, training=self.training)
        v5  = self.qk(vk).transpose(-2, -1)
        return v5


# Initializing the model