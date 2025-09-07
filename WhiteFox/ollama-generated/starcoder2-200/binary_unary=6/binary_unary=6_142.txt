
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20, bias=False)
        self._other = nn.Parameter(Tensor(3).fill_(5))
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 - self._other  # Subtract 'other' from the output of the linear transformation 
        v3 = F.relu(v2) # Apply the ReLU activation function to the result
