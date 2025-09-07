
class Model(torch.nn.Module):
    def __init__(self, inplanes=64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(inplanes, 3, kernel_size=(5, 5), stride=2)

    def forward(self, input):
        input = self.conv1(input)

        # A fused operation would be added here if the previous line was used without using torch._C.fuse_conv_bn 
        return input


m = Model()

# Input to the model
x = torch.rand(2, 3, 57, 41)

