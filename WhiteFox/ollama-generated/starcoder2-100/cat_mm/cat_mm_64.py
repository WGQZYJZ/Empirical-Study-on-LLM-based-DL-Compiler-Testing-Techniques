

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.mm(x1, x2) # Matrix multiplication of two input tensors 
        v2  = self._cat(v, repeat_time=4) # Concatenation along the first dimension. The number of concatenations depends on repeat_time argument.
        return v2
 
    def _cat(self, v, repeat_time):
         for i in range(repeat_time):
             v3 = torch.cat([v] * 16, dim=0) # Repeat the input tensor along a dimension. The number of times repeated depends on repeat_time argument
         return v


# Initializing model instance