
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.permute(x1, 0, 3)  # Permute tensor A
        v2  = torch.bmm(v1, x2)  # Matrix multiply tensor B with tensor A permuted
        return v2


# Initializing the model
m  = Model()


# Inputs to the model (different from the previous one):
x1  = torch.randn(3, 4, 5, 6)  # input_tensor_A
x2  = torch.randn(7, 8)        # input_tensor_B

 __output__  = m(x1, x2)