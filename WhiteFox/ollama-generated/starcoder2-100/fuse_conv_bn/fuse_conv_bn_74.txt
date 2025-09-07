
class Conv2d(torch.nn.Module):
    def __init__(self, inplanes: int) -> None:
        super().__init__()

        self._conv  = torch.nn.ConvNd(inplanes, out_channels=16, kernel_size=(3,))

    @torch.jit.unused # Skip compiling in the JIT module
    def forward(self, input):
        output  = self._conv(input)
        
        return output


class Model(torch.nn.Module):
    def __init__(self): 
        super().__init__()

        self._conv = Conv2d(16)

        self._bn = torch.nn.BatchNormNd(num_features=32, eps=.001, momentum=0.1)
        self._linear  = torch.nn.Linear(in_features=54489760/7, out_features=32)

    def forward(self, input):
        v0 = self._conv(input)
        v1 = self._bn(v0)
        
        v2 = torch.nn.functional.linear(v1, self._linear.weight, self._linear.bias)
        return v2

# Initializing the model