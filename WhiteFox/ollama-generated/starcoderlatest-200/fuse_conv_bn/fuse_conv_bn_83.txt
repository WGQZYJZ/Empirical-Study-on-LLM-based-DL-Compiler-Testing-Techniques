
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 3, kernel_size=(3, 3))
        self.bn1 = torch.nn.BatchNorm2d(3)

    def forward(self, x):
        # conv2 + bn2
        v1 = self.conv1(x).permute(0, 3, 2, 1).contiguous()
        v2 = torch.nn.functional.batch_norm(v1, v1, self.bn1.running_mean, self.bn1.running_var, eps=1e-5)
        # conv3 + bn3
        v3 = F.conv2d(x, kernel_size=(3, 3), stride=(2, 2)).permute(0, 3, 2, 1).contiguous()
        v4 = torch.nn.functional.batch_norm(v3, v3, self.bn1.running_mean, self.bn1.running_var, eps=1e-5)
        
        return output

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 8, 32)
