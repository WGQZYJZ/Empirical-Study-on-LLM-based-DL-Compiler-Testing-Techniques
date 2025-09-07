
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv1d(in_channels, out_channels, kernel_size=kernel_size) # 1d conv
        self.bn    = torch.nn.BatchNorm1d(out_channels)
    def forward(self, x):
        v1  = x.permute((0, 2, 1))
        v2  = torch.nn.functional.conv1d(v1, self.conv.weight, bias=self.conv.bias, stride=stride, padding=padding) 
        v3  = self.bn(v2) # bn tracks running mean and std; this runs the batch norm in eval mode.
        return v3

# Initializing the model
m1  = ConvBnModel()

