
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        v1  = x1.permute(0, 2, 1) 
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3  = input_tensor_A.permute(...) 

        v4  = input_tensor_B.permute(...)

        v5  = torch.bmm(v2, t3)
        return v5


# Initializing the model