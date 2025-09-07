
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v1  = self._conv(x1)
        v2  = torch.relu(v1 + self.other)
        return v2
        
    @staticmethod
    def _conv(input_tensor):
        conv_func()
        return input_tensor

m = Model()

