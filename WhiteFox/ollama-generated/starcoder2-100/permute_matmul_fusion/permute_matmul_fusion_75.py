
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      t1 = torch.randperm(3)
      v1  = x1.permute(0, [t1[2], t1[0]]) # Permute the input tensor
      t2 = torch.randperm(5)
      v2  = v1.permute([t2[-1], t2[-4], t2[-3]]) # Permute the permuted tensor V1, and then permute the permuted tensor again to swap the dimensions 0 and 1 of this permuted tensor, which is V2
      v3 = torch.bmm(v2, x) 
      return v3

# Initializing the model
m = Model()

