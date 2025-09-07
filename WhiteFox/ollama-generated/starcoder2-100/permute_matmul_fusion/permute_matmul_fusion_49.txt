
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1 = torch.randn(2, 3) # Input tensors of the permute method 
        v2 = x1.permute([0, 2, 1]) 
        v3 = torch.bmm(v2, v1)
        
        v4 = y1.permute([0, 2, 1])
        v5 = torch.matmul(y1, v1).transpose(-2, -1)
        return torch.cat((v3, v5), dim=0)[-x1.shape[0]:]


# Initializing the model
m = Model()

# Inputs to the model
input_tensor_A  = torch.randn(3, 2, 4)
input_tensor_B  = torch.randn(5, 2, 7)
x1, y1          = input_tensor_A[0], input_tensor_B[0]

__output__      = m(x1, y1)

