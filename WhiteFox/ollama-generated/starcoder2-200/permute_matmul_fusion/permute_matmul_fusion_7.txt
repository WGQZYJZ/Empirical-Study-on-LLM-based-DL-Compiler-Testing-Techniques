
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 3) # Permute the input tensor A by swapping its first and third dimensions.
        v2 = torch.bmm(v1, self.linear_layer) # or torch.matmul(x1, x2)
        return v2


# Initializing model
m = Model()
# Inputs to the model
x1  = torch.randn(3, 4, 5, 6) # input A with more than two dimensions (not 2d)
x2  = torch.randn(3, 7, 8, 9) # input B
__output__  = m(x1, x2)

