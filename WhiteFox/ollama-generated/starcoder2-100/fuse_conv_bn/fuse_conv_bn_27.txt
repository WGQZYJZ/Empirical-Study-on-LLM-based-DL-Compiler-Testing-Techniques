
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv  = torch.nn.Conv2d(3, 4096, (7, 7), stride=(2, 2), padding=(3, 3))
        bn = torch.nn.BatchNorm2d(num_features=4096)

        v1 = x1.permute(0, 2, 1).contiguous() # Conv expects the channels as the first dimension (channel 1)
        v1  = conv(v1)
        v1  = bn(torch.nn.functional.relu(v1))
        return v1

m_convbn = ConvBnModel()


x1 = torch.randn(1, 3, 28, 28) # The shape of the input is (N, C, H, W), where N stands for batch size, C represents channel dimension, and H and W represent height and width dimensions respectively.
