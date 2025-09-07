
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
       # First permute the input tensor A.
       v3 = torch.nn.functional.linear(x1.permute(0, 1), self.linear.weight, self.linear.bias)

       # Then perform bmm with a permuted and un-permuted input tensors. 
       # You can also call bmm with 2 input tensors which will be automatically swapped.
       # v4 = torch.bmm(x1.permute(0, 1), x2) 
       v5 = torch.matmul(v3, x2) 
       return v5

# Initializing the model
m = Model()

