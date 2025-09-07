
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 40, 7)
        bn = torch.nn.BatchNorm2d(40)
        
        v1 = bn(conv(x1))
        return v1


m  = Model()
# Input tensors with 5 dimensions
input_tensor  = torch.randn(2, 3, 16, 9, 7)
input_tensor_newsize  = input_tensor.permute(0, 2, 3, 1).clone() # Change to the new size [2, 4, 15]

__output__  = m(x1)