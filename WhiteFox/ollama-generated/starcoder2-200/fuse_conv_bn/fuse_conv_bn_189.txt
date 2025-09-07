
class MyModel(nn.Module):
    def __init__(self, **kwargs) -> None:
        super().__init__()

        self._conv = nn.Conv2d(**kwargs)
        self._bn   = nn.BatchNorm2d(3)

    def forward(x):
       output = torch.nn.functional.batch_norm(torch.nn.functional.conv2d(input, self._conv),
            weight=self._bn.weight, bias=self._bn.bias, running_mean=self._bn.running_mean, running_var=self._bn.running_var)
       return output

# Initializing the model 
m = MyModel()


# Inputs to the model 
input  = torch.randn(1, 3, 256, 256).to('cuda:0')
