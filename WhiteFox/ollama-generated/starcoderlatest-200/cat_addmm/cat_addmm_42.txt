
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
        self.mat1 = torch.nn.Parameter(mat1)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, None)
        v2 = torch.cat([v1], dim=-1)
        return v2

# Random initialization for the weight tensor mat1 of shape (3, 8), and random initialization for the bias tensor mat2 of shape (8,)
mat1_initial = torch.rand(3, 8)
mat2_initial = torch.rand(8)
# Initializing the model with randomly initialized mat1 and mat2
m = Model(mat1_initial, mat2_initial)


def get_weights(model):
    weights_list = []
    for w in model.parameters():
        weights_list += [w]
    return torch.cat(weights_list, dim=-1)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
