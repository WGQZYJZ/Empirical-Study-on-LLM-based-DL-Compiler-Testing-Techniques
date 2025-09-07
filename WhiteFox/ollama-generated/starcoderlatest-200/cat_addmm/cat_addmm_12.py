
class Model(torch.nn.Module):
    def __init__(self, mat1=None):
        super().__init__()
        self.input = torch.randn(32)
        if mat1:
            self.mat1  = torch.tensor([1., 0., -1.], dtype=torch.float) 
            self.mat2  = torch.tensor([-1., 2., 1., 4.], dtype=torch.float).reshape((2, 2))
            self.input = self.input + torch.mm(self.input, self.mat1)
            self.input = self.input + torch.t(self.input) * torch.diag_embed(self.input[:, [0]]) 
            self.input = self.input + self.mat2
            self.input = self.input.to(torch.long)
        self.cat  = torch.tensor([1.], dtype=torch.float).reshape((1, ))

    def forward(self):
        t1  = torch.addmm(self.input, self.mat1, self.mat2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2  = torch.cat([t1], dim=0) # Concatenate the result along dimension zero 
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8)
