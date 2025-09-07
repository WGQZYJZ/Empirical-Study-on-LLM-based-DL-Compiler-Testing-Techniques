
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.conv(x1) + self._other_tensor # Where _other_tensor is another tensor specified by the keyword argument "other"
        return v1
