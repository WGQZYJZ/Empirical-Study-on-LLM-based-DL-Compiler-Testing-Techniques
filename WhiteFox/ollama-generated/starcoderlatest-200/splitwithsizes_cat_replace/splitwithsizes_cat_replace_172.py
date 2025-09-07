
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
      t0 = torch.split(x1, 64, dim=3)
      v1 = self.__make_tensor_conv_sum(t0[0], t0[1]) 
      v2 = torch.cat([v1, x2], dim=-1)

      return v2

def __make_tensor_conv_sum(x, y):
  v  = x * y 
  v += x + y
  
  return v

  