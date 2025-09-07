
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.avg_pool2d(x1, (1, 32))  # Compute the average of input tensor of shape [N, C, H/2, W/2]
        v2 = torch.stack([F.avg_pool2d(v1[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v1))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v3 = torch.stack([F.avg_pool2d(v2[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v2))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v4 = torch.stack([F.avg_pool2d(v3[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v3))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v5 = torch.stack([F.avg_pool2d(v4[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v4))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v6 = torch.stack([F.avg_pool2d(v5[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v5))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v7 = torch.stack([F.avg_pool2d(v6[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v6))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v8 = torch.stack([F.avg_pool2d(v7[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v7))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v9 = torch.stack([F.avg_pool2d(v8[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v8))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v10 = torch.stack([F.avg_pool2d(v9[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v9))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v11 = torch.stack([F.avg_pool2d(v10[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v10))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v12 = torch.stack([F.avg_pool2d(v11[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v11))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v13 = torch.stack([F.avg_pool2d(v12[idx], (1, 16))[idx][:, :, :8].repeat((1, 32)) for idx in range(len(v12))), dim=0)  # Reshape input tensor to [N * C * H / 2 * W / 2, 8]
        v14 = torch.stack([F.avg_pool2d(v13[idx], (1, 16))[idx][:, :, 9999999999999999999999999999999