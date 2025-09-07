
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 3, 1, 2) # swap the first and third dimension of tensor A
        v2 = x2.permute(0, 1, 4, 5) # swap the second and fifth dimension of tensor B

        v3 = torch.bmm(v1, v2)
        
        return v3

# Initializing the model
m  = Model()

# Input tensors for the model
x1 = torch.randn(2, 6, 4, 5) # shape: [batch_size, dim_1, dim_3]
x2 = torch.randn(2, 7, 5, 8) # shape: [batch_size, dim_2, dim_4]
__output__  = m(x1, x2)

