
class Model(torch.nn.Module):
    def __init__(self, add):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + add
        return v2

# Initializing the model with an addition operation that adds two tensors to its output
add_tensor  = torch.randn(3,8,64,64)
add_tensor1 = torch.randn(3,8,64,64)
m  = Model(add=add_tensor + add_tensor1)

 # Inputs to the model with both tensors being passed as keyword arguments. These tensors will be added together by torch.nn.functional.conv2d() and then passed to torch.nn.Conv2d() as an input tensor, followed by torch.nn.functional.add().
x1  = torch.randn(1,3,64,64)

 # Outputs produced by the model with the addition operation. The model output is both tensors added together and passed to torch.nn.functional.conv2d() and then added together again.
