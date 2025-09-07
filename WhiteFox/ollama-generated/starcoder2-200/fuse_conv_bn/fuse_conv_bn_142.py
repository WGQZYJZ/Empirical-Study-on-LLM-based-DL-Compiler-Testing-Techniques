
import torch 
import torch.nn as nn
class Model(nn.Module):
    def __init__(self,  n = 4):
        super().__init__()
        self.conv1 = nn.Conv2d(3,n//2 ,kernel_size=7) 
        self.conv2 = nn.Conv2d(n // 2 + 3, 80, kernel_size=7)
    
    def forward(self, x):
      v4 = torch.nn.functional.conv2d(x, self.conv1.weight)
      v5 = torch.nn.functional.batch_norm(v4, affine=False) 
      return nn.functional.conv2d(x + 10 ,self.conv2.weight).sigmoid()

model = Model().cuda()
x = torch.rand([3,80] + [5]*3 ).float().cuda() # 5 for input size for conv2 
print(model(x))

<|> 
