
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(8, 64)
        self.key   = torch.nn.Linear(128, 512)
        self.value = torch.nn.Linear(3072, 4096)
 
    def forward(self, query):
        scale_factor  = 1 / math.sqrt(query.size(-1))
        vq  = self.query(query).unsqueeze(-1) # [N, C, K]
        vk  = self.key(self.key).permute([0,2,3,1]) # [N, K, C, M]
        vv  = self.value(query.reshape(-1, query.size(-1))).view_as(vk) # [N, K, M, M]
 
        kq  = vq * scale_factor # [N, C, M, M]
        qk  = kq.permute([0,3,2,1]) # [N, M, M, C]
        dotprod  = torch.matmul(qk, vk) # [N, M, M, M]
        scaled_dotprod  = dotprod.mul(scale_factor) # [N, M, M, M]
        softmax  = scaled_dotprod.softmax(-1) 
        vq  = dropout(softmax, dropout_p).matmul(vv) 
        return vq


# Initializing the model
m  = AttentionModel()
 
# Inputs to the model
query = torch.randn(4096, 32768)

__output__  = m(query)