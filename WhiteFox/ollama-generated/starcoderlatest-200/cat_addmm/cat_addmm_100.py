
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.tensor([[0.5, 0], [-0.5, -1]], dtype=torch.float)
        self.mat2 = torch.tensor([[-0.7071067811865476], [0.7071067811865476]], dtype=torch.float)
 
    def forward(self, x1):
        t1  = torch.addmm(x1, self.mat1, self.mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2  = torch.cat([t1], dim=0) # Concatenate the result along dimension zero
        return t2
 
