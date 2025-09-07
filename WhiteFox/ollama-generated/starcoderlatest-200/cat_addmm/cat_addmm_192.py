
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm = torch.nn.Addmm(1, 8, 3)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.w_mat1, self.b_mat1)
        v2 = torch.cat([v1], dim=0)
        return v2

    def get_params(self):
        return [self.w_mat1, self.b_mat1]


# Generating the input tensor for the newly generated model
x1 = torch.randn(2, 3, 64, 64)

# Parameters to initialize the new model
self.w_mat1 = torch.tensor(v1)
self.b_mat1 = torch.tensor(v5)


