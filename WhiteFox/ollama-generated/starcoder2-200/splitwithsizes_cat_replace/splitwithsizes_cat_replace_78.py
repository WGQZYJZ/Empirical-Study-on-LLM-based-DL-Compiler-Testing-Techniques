
class Model(torch.nn.Module):
    def __init__(self, num_classes=1000, pool_features=256):
        super().__init__()
        self.pool = torch.nn.AdaptiveAvgPool2d((1, 1))
 
    def forward(self, x):
        self._modules["global_pool"]  =  self.pool
        return torch.mean(x, dim=[-3, -2], keepdim=True)


