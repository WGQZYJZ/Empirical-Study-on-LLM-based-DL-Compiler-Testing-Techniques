
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 32, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # First and second conv layers
        v1  = self.conv1(x1)  # (B, C_in, T, H) -> (B, C_in, H, W)
        v2  = self.conv2(v1)  # (B, C_in, H, W) -> (B, C_in, C_mid, D)
        v3  = self.conv3(v2)  # (B, C_in, C_mid, D) -> (B, C_in, C_out, H')

        # Second conv layer -> (B, C_in, C_out', W')
        v4  = F.linear(v3, self.attn_weight, bias=self.bias)   # Linear with weight and bias
        output = torch.cat([v1, v4], dim=1) # B, C_mid + C_out' (C_in + C_out')

        return output


# Initializing the model
m = Model()

