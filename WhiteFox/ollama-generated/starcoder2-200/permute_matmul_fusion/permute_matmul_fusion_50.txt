
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.bmm(x1.permute(0, 2, 1), self._x2) # This is used for scenario 1 or scenario 3.
        return v1

# Initializing the model and inputs to the model:
m = Model()

input_tensor_A = torch.randn(5, 4, 3)
input_tensor_B = torch.randn(5, 3, 2) # This will be permuted at the first permute call by the pytorch function permute of a 5-by-3 tensor.
__output__  = m(x1=input_tensor_A, x2=input_tensor_B)


