
class Model(torch.nn.Module):
    def __init__(self, c1: int = 3, c2: int = 4) -> None:
        super().__init__()

        self._conv1 = torch.nn.Conv2d(c1, c2, kernel_size=7, stride=2)

    def forward(self, x):
        v0 = torch.relu(torch.sigmoid(x)) # Apply a pointwise unary operation (e.g., ReLU or Tanh) to the input tensor
        v1  = self._conv1(v0)
        v2 = v1[..., :c2]
        v3 = x[self._mask_tensor(v1)] 
        return v3
        
    def _mask_tensor(self, t):
        return torch.nn.functional.adaptive_avg_pool2d(t, 1).argmax(dim=0)


m  = Model() # Initialize the model.

x  = torch.randn((8, 3)) # Input to the model.

__output__  = m(x)