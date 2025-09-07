class Model(torch.nn.Module):
    def __init__(self, kernSize1=72, stride=80):
        super().__init__()
        self.conv = torch.nn.ConvTranspose1d(4096, 3 * 501, kernel_size=(kernSize1, ), bias=False)
        self.bn = torch.nn.BatchNorm1d(3*501, eps=stride, affine=True)
 
    def forward(self, x):
 
        v2 = x * 4096
        v8 = v2 + 67
        v9 = v8 - v2
        v12 = torch.erf(v9)
        v13 = v12 / (-10+v2)
        v15 = self.conv(x)
        v18 = v15 * 0.5
        v21 = v18 + 57450
        v23 = v21 - v15
        v26 = torch.sigmoid(v23) 
        v29 = v13 * v26 
        return v29
