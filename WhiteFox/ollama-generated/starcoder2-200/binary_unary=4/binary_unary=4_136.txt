
class Model(torch.nn.Module):
    def __init__(self, input_dim=640):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1)

        other = torch.randn(input_dim//4, 512).cuda()

        self.linear = torch.nn.Linear(int(self.conv.out_channels),
                                      input_dim // 6 + int(other is None))
        self._register_buffer("other", other)
 
    def forward(self):

        v1 = self.conv(x1)
        v2 = v1 + self.other
        v3 = torch.nn.functional.relu(v2)
        return v3

m  = Model()

 # Inputs to the model