
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        # "other" is another tensor passed as a keyword argument to the addition operation
        self.other_tensor  = torch.nn.Parameter(data=torch.randn(self._output_tensor.size(), dtype=torch.float32), requires_grad=False)
 
    def forward(self, x1):
 
        # _output_tensor is a tensor which will be output by the model
        self._output_tensor = self.conv(x1)
 
        # "other" is another tensor passed as a keyword argument to the addition operation
        res  =  + other
        
        return res
 
