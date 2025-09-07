
class Model(torch.nn.Module):
    def __init__(self, bmm=False):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1 if not bmm else torch.randn_like(x1).permute(-1, -2) # Permute the input tensor 1
        v2 = x2 if not bmm else torch.randn_like(x2).permute(-3, -4) # Permute the input tensor 2
        if bmm:
            result = torch.bmm(v1, v2)
        else:
            result = torch.matmul(v1, v2)

        return self.linear(result), x1


m  = Model()


# Inputs to the model
x1_permute = True # Permute or not permute input tensor A; boolean variable that defaults to False for non-permuted input and True if it's permuted.
bmm = False       # Whether use bmm operation, or torch.matmul  # boolean variable that defaults to False for multiplication by matrix and True for batch matmul.


x1_input = x2_input = torch.randn(3, 4)
if x1_permute:
    x1_input = torch.randn(3, 5).permute(-1, -2)
if bmm:
    x2_input = torch.randn(3, 4, 6).permute(-1, -3) # Permute the input tensor B
    
__output__, __input_tensors__ = m(x1_input, x2_input)

