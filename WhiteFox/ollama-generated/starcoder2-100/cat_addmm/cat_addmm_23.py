
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2, dim3):
        super().__init__()

        self.fc = torch.nn.Linear(dim1, 4 * dim2)

    def forward(self, x):
      v0 = torch.full([7, dim2], float('nan'), device=x1.device).to(x1.dtype)
      v1 = torch.addmm(v0, self.fc._parameters['weight'].T, self.fc._parameters['bias'])
      
      v2 = x.new_empty((7, 4 * dim3), dtype=self.fc._parameters['weight'].dtype).copy_(x1)
      v3 = torch.cat([v1, v0], -1)
      
      return v2

# Initializing the model
dim1, dim2, dim3 = 64, 5, 78
m = Model(dim1, dim2, dim3).to('cuda')
x1 = torch.randn(7, 90, 64)
