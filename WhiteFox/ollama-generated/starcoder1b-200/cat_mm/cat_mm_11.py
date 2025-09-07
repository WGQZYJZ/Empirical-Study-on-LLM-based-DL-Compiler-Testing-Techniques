
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2)
 
    def forward(self, x1):
        # x1: [B, C, H, W] => [B, C*K*H*W, H*W]
        v1 = self.conv1(x1).view(x1.size(0), -1)  # [-1, 8*K*H*W], size of the input tensor is [-1, K*H*W]
        v2 = v1 + v1 + v1 + v1   # [B, K*H*W, H*W], element-wise add to get [B, H*W, 8*K*H*W]
        v3 = self.conv2(v2).view(x1.size(0), -1)  # [-1, 16*K*H*W], size of the input tensor is [-1, K*H*W]
        v4 = v3 + v3 + v3 + v3   # [B, K*H*W, H*W], element-wise add to get [B, H*W, 16*K*H*W]
        return v4


# Initializing the model
m = Model()

