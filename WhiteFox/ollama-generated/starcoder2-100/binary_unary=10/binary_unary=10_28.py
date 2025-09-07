
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Initialize input_tensor with shape (32, 512) with uniform distribution and fills other elements randomly.
        # Input size is a 3d tensor, and the second dimension will be determined by the user.
        self._input = torch.randn(32).uniform_(0, 1)
 
        # Initialize other_tensor with shape (32, 512) with uniform distribution and fills other elements randomly.
        # Input size is a 3d tensor, and the second dimension will be determined by the user.
        self._other = torch.randn(32).uniform_(0, 1)
 
    def forward(self):
        v1  = F.linear(input=self._input, weight=self._other)
        v2  = v1 + other_tensor
        v3  = F.relu(v2)
