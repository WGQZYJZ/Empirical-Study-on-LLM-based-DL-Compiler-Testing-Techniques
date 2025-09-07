
class Module(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.conv = torch.nn.ConvNd(dim) 
        self.bn   = torch.nn.BatchNormNd(dim)

    def forward(self, x1):
        v2  = conv(x1).to(dtype=torch.double) # to() should have the argument 'device' set
        v3  = torch.nn.functional.batch_norm(v2, self.bn.running_mean, self.bn.running_var,
                                              None, None, self.bn.eps).to(self.conv.weight.dtype) 
        return v3

# Initializing the model
m  = Module(dim=10) # dim should match the ConvNd and BatchNormNd argument

