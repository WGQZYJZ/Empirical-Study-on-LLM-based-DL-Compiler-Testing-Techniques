
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, k, v):
        query_feature = self.conv(x1).view(-1, x1.shape[0], -1) # Shape: (B, N, F) where B is batch size and N is the number of patches and F is the number of channels in each patch
        value_feature = v.view(1, 1, v.shape[0], v.shape[1]) * self.conv(k).view(1, k.shape[1], -1) # Shape: (B, 1, K, V) where B is batch size and K and V are the number of keys and values in each patch
        # Shape: (B, N, F) where B is batch size and N is the number of patches and F is the number of channels in each patch
        return torch.matmul(query_feature, value_feature).view(x1.shape[0], -1)


# Initializing the model
m = Model()


