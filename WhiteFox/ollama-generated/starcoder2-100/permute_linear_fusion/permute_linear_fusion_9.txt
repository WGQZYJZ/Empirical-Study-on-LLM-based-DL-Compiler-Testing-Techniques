
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3  = torch.nn.functional.linear(x1, self.linear.weight)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(3,4).unsqueeze(-1) # add a 1-dim tensor to create 3D input_tensor
__output__  = m(x2)

# Results

| Name | Description | Value | Expected Value | Result | Diff | Type | Message |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| [0] | - | torch.Size([3, 4]) | 1 | <class 'torch.Tensor'> | <class 'torch.Size'> | | |
| [2] | - | torch.Size([]) | 0 | <class 'int'> | <class 'torch.Size'> | | |

