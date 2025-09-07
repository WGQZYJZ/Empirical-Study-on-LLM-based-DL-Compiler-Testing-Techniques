
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=1)

    def forward(self, x1):
        # (N, C_in, H, W)
        v1 = self.conv1(x1)  # B
        # (N, C_in, H', W') -> (N, C_in', H' ,W')
        v2 = torch.nn.functional.avg_pool2d(v1, kernel_size=v1.shape[-2:])  # C
        # (N, C_in', H', W') -> (N, C_out, H ,W)
        v3 = self.conv2(torch.nn.functional.dropout(v2, p=self.drop))  # B
        return v3


# Initializing the model
m = Model()


