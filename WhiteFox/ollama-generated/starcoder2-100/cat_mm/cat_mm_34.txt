
class Model(torch.nn.Module):
    def __init__(self, t1: int = 320) -> None:
        super().__init__()

        self.conv0 = torch.nn.Conv2d(3, t1//8, kernel_size=5, stride=4)
        self.conv1 = torch.nn.Conv2d(t1//8, t1//4, 1)
        self.conv2 = torch.nn.Conv2d(t1//4, t1//4 * 3, kernel_size=(7,5), stride=6, padding=[0,0])
        self.norm  = torch.nn.LayerNorm([48] + [t1//4 for i in range(int(log(input_size/4)))], elementwise_affine=True)

        self._loss = nn.L1Loss()

    def forward(self, x: torch.Tensor):
        v0  = self.conv0(x)
        v1 = F.max_pool2d(v0, kernel_size=(7,5), stride=[3] + [i//8 for i in v1[0].shape], padding=9*[0])
        v2  = torch.mm(self.norm(F.max_pool2d(v1, kernel_size=1)), v1)
        v3 = torch.cat([t1]*50, -1)
        loss = self._loss(v2, v3)
        return loss

# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn((87, 9), 34344)

# Outputs from the model
__output__  = m(x1)


