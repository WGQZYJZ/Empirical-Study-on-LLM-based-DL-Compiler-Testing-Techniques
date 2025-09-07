
class Model(torch.nn.Module):
    def __init__(self, split_sizes=[32]):
        super().__init__()
        self.split = torch.nn.Split(1)
        self.concat = torch.nn.Concat([1] * len(split_sizes))

    def forward(self, x1):
        v1  = self.split(x1)

        v2  = [None for _ in range(len(v1))]
        for i in range(len(v1)):
            v3  = torch.nn.ZeroPad2d((0, split_sizes[i], 0, 0))(v1[i])
            v4  = self.conv(v3)
            v5  = [torch.nn.AvgPool2d(kernel_size=4), torch.nn.Upsample(scale_factor=split_sizes[i] // 4)]
            v6  = torch.nn.Sequential(*v5)(v1[i])

            v7  = v3 + v4 + v6
            v2[i]  = [torch.nn.ConvTranspose2d(8, in_channels=len(split_sizes) * split_sizes[i], kernel_size=(5, 5)), torch.nn.Flatten()]
            v7  = self.conv(*v2[i])

            v8  = self.concat([v1[i] for i in range(len(v1))])
            return [torch.nn.ConvTranspose2d(in_channels=split_sizes[0], out_channels=sum(split_sizes), kernel_size=(5, 5)), torch.nn.Flatten()]
        v9 = self.conv(*v8)
