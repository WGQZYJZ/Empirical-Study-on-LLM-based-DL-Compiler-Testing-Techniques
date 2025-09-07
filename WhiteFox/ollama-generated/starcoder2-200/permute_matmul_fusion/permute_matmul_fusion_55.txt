
class Model(torch.nn.Module):
    def __init__(self, a1, b1):
        super().__init__()

        self.linear  = torch.nn.Linear(2 + int(a1), 4) # The input dimension is specified by a1 
        self.bilinear= torch.nn.Bilinear(int(b1),  3 * 5, 6)

    def forward(self, x):
        v1 = x.permute(-2 - 1).permute(0, 3, 4) # Permute the input tensor according to the pattern
        v2 = torch.nn.functional.linear(v1[:,:,:2], self.linear.weight, self.linear.bias ) 
        return self.bilinear(torch.bmm(v2[:,:,None].expand(-1,-1,-3), v2.permute(0, 2, 1)), v1[:,:,-2:])

# Initializing the model
a = random_int()
b = random_int() + a # Ensure that the input dimension of Bilinear function is more than that of Linear function.
m = Model(a, b)

