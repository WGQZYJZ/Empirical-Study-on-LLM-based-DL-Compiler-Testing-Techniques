
class Model(torch.nn.Module):
    def __init__(self, n_list):
        super().__init__()
        self.n_list  = n_list
        self.n_list[0] +=1
 
    def forward(self, x1): 
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1 for _ in range(self.n_list[0])], dim=4) # Concatenate the matrix multiplication result along dimension 5
        return v2


# Initializing the model with a list of length four
m  = Model(n_list=[4,7,8,3]
)
 
# Inputs to the model
x1 = torch.randn(4, 64, 64, 64, 5) # Input tensor x1 of shape [N, H, W, D, 5], where N is batch size
x2 = torch.randn(7, 8, 3, 64, 64) # Input tensor x2 of shape [C, H, W, 64, 64]
 
__output__  = m(x1) # Output of the model

