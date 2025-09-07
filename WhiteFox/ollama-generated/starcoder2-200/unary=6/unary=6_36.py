
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6) 
        v5 = v1 * v4
        v6 = v5 / 6
        return v6

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

## Please provide a PyTorch example that meets the following conditions:
- It contains operations on tensor.permute, transpose or flatten
- The input to the model should not be used twice in the model
- Use a namedtuple to store the intermediate values of each operation (see more info [here](https://docs.python.org/3/library/collections.html#collections.namedtuple)). The output values should follow the naming format v1, v2 ...
- The input tensor should be stored in the input variable x_
- A method is used to generate a tuple of operations (see more info [here](https://docs.python.org/3/library/typing.html#typing.NamedTuple)) 
- You should use at least one operation from the following: permute, transpose, flatten and cat
