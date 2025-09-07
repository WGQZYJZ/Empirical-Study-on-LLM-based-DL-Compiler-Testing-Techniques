
class Model(torch.nn.Module):
    def __init__(self, t1=None):
        super().__init__()

        self.linearA = torch.nn.Linear(2, 2)
        self.linearB = torch.nn.Linear(2, 2)

        self.permute_t1  = lambda x:x.permute(-2,-3,-4,)
        self.permute_t2  = lambda x:x.permute(-5,-6,-7,)
        self.permute_t3  = lambda x:x.permute(0, -8)
        self.permute_t4  = lambda x:x.permute(-19,-18,0)

        self.matmulA  = torch.nn.functional.linear(self.permute_t2(input_tensor), self.linearA.weight, self.linearA.bias)
        self.matmulB  = torch.nn.functional.linear(self.permute_t4(input_tensor), self.linearB.weight, self.linearB.bias)
        self.matmulAB = torch.bmm(self.matmulA, self.matmulB,)

        self.matadd  = t1 + (self.matmulAB,)
        return self.matadd

# Initializing the model with a non-empty input tensor
t3   = Model(input_tensor)

