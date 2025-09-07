
class Model(torch.nn.Module):
    def __init__(self, conv1=torch.nn.Conv2d(3, 8, 1), conv2=None):
        super().__init__()
        self._conv1 = conv1
        if conv2 is None:
            conv2 = torch.nn.Conv2d(50, 476, 1)
        self._conv2 = conv2
 
    def forward(self, x1):
        v1  = self._conv1(x1)
        v2  = v1 - other  # Subtraction between the output of 'v1' and another tensor (referred to as 'other')
	v3  = self._conv2(v2)
        return v3

