class Model(torch.nn.Module):
    def __init__(self, input1_, input2_, num_):
        super().__init__()
        self.linear = torch.nn.Linear(input1_.shape[0], 3*num_)

    def forward(self, x1, x2):
      x = self.linear(x1)
      x = x[:, :96] # Select the first 4 dimensions from each matrix multiplication result tensor
      return torch.cat([x]*8+[x*0])
