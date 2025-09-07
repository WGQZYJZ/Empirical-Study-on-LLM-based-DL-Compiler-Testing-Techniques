
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Input 1 is a scalar value and input 2 is an image with size [BxCxHxW]
        return self._func_1(x1) @ self._func_2(x2)
 
    def _func_1(self, x1):
        return torch.matmul(x1, x1.transpose(-2,-1))
    
    def _func_2(self, x1):  # Input 3 is an image with size [BxCxHxW] and Input 4 is an image with size [B, CxDxHxW].
        B1 = torch.nn.ReLU()(torch.conv1d(x1, kernel=self._conv_weight, stride=2))
        B2 = torch.sigmoid()(torch.bmm(x3.permute(-1,-2), self._attn_weight) @ x4 + self._bias_1)
        return torch.cat((B1, B2), 0)


# Initializing the model
m  = Model()

