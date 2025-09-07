
class Model(torch.nn.Module):
    def __init__(self, d1=4096):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 5)
        self.bn   = torch.nn.BatchNormNd(num_features=5)

    def forward(self, x):
      v = torch.nn.functional.conv2d(x, self.conv.weight, bias=None, padding=1) # pad 0 on all 4 sides
      return torch.nn.functional.batch_norm(v, self.bn.running_mean, self.bn.running_var, affine=True)

m = Model()

