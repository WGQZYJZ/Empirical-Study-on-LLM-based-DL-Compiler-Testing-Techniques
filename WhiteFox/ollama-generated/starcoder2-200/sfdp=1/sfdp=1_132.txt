

## 1-D Conv Model

class Conv1DModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self._conv = torch.nn.Conv1d(3, 8, 1)

    def forward(self, x):

        x = F.dropout(x, p=0.5) # Apply dropout to input before the conv1d operation is applied
        return self._conv(x)

## 2-D Conv Model 

class Conv2DModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self._conv = torch.nn.Conv2d(3,8,1)

    def forward(self, x):

        return self._conv(x)

