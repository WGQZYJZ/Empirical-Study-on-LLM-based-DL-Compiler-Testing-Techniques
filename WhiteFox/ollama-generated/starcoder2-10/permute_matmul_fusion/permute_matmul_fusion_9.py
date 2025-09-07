
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor A

        v1  = x1.permute(0, 2, 1)
        v2  = x2.permute(0, 2, 1)
        v3  = torch.bmm(v1, v2).permute(0, 2, 1) # or torch.matmul(v1, v2).permute(0, 2, 1), the input tensor A and B is swapped

        return v3

# Initializing the model
m = Model()


# Inputs to the model - 3 different models to test different scenarios of swapping the inputs.
x1A  = torch.randn(4096,  2) # input_tensor A shape: (batch_size, N, M) where 2 <= N < 5 and 1 <= M <= N
x1B  = torch.randn(378,   2) # input_tensor B shape: (batch_size, P, Q) where 3 <= Q <= 6 and P >= 2
__output__A  = m(x1A, x1B) # forward on the model with input tensor A and input tensor B
__output__B  = m(x1B, x1A) # forward on the model with input tensor B and input tensor A

