
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 90, 72)
__output__  = m(x1)

- [Github](https://github.com/ratsgo/torchgendoc/tree/master/%EC%B5%A0%EB%AC%BC%ED%94%84%EB%A1%9C%EC%A7%80)
- [Github Markdown syntax reference](https://github.com/ratsgo/torchgendoc/tree/master/%EC%B5%A0%EB%AC%BC%ED%94%84%EB%A1%9C%EC%A7%80%20Markdown%20%EA%B3%BC%ED%95%A9%20%EC%BD%94%EB%93%9C)