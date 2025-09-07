
class Model(torch.nn.Module):
    def __init__(self, k, n):
        super().__init__()
        self.linear  = torch.nn.Linear(k,n)
 
    def forward(self, x1):
        v2  = torch.mm(x1, x1) # 矩阵乘法
        v3  = torch.cat([v2 for i in range(4)], dim=0)# 沿着第三个维度进行了4次拼接，相当于对原始张量重复四次。（第四个参数dim: 拼接维度的索引值）
        return self.linear(v3) # 最后添加全连接层
# Initializing the model
m = Model(10, 256)
__output__  = m(torch.randn(4,10))

