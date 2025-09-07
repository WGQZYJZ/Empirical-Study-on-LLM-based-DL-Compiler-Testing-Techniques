def  __init__(self):
    super().__init__()
    self.linear1 = torch.nn.Linear(2, 2)
    self.dropout1 = torch.nn.Dropout(0.5)
    self.linear2 = torch.nn.Linear(2, 3)

  def forward(self, x1):
      v1 = self.dropout1(x1) # Apply dropout to the input tensor
      v2 = self.linear1(v1) # Apply linear transformation to the permuted tensor.
      v4 = torch.rand_like(v2) # Generate a new random tensor with the same size as input tensor filled with random numbers
      v5 = self.linear2(v2 + 50*self.dropout1(x1) + self.dropout1(3*x1)) 
      return v4, v5
