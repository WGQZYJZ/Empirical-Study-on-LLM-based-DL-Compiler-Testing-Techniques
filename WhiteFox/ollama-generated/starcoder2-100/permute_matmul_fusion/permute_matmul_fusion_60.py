
class Model(torch.nn.Module):
    def __init__(self, B_size: int = 32):
        super().__init__()
        self.linear1  = torch.nn.Linear(480, B_size * B_size)
        self.linear2  = torch.nn.Linear(B_size, 3)

    def forward(self, input_tensor: torch.Tensor, B):
       permute  = input_tensor.permute(-1, -2).contiguous() # Permute the input tensor.
       v1      = self.linear1(input_tensor) + self.linear2(B)
       v2  = torch.bmm(v1, permute)
        return v2

# Initializing the model and setting hyperparameters/initial inputs
m  = Model()


x1 = torch.randn(3405, 768)
x2 = torch.randn(B_size=32, 97, 97).cuda()
x3 = torch.randn(3405, B_size=32, 97) # In the first dimension of input tensor B should be equal to the first dimension of the output tensors after the permute.
__output__   = m(input1, x2)

