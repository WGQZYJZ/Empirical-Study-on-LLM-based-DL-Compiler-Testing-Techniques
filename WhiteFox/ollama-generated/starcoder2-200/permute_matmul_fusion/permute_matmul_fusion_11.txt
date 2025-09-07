
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
      # Permute the input tensors first before performing bmm
      t1 = torch.transpose(x1, 0, -1)
      t2 = torch.transpose(torch.bmm(t1, x2), 0, -1).permute(0, 2, 3, 1)

      # Alternatively, we can also permute the input tensors after performing bmm directly (as in this example)
      return torch.transpose(x1, 0, -1), t2

m = Model()

# Inputs to the model with two input tensors A and B
x1  = torch.randn(3, 4, 5) # The shape of x1 is [N, B, C] (The permutation of [N, C, B] does not affect the result of matrix multiplication)
x2  = torch.randn(4, 3, 8) # The shape of x2 is [B, D, E] (The permutation of [D, E, B] also does not affect the result of matrix multiplication). 

__output__, __output1__,  __output2__, __output3__, = m(x1, x2)
