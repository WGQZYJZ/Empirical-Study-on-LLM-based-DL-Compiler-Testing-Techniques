
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)

        # This code will not work because the tensors are not batched (batch-matmul is only available for 2+D tensors).
        #v3 = torch.bmm(v1, v2) 

        # The following two lines of code should work as expected, and this would give the same result as the previous line of code. 
        v3 = torch.matmul(v1, v2) 

        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 2, 3) # Batch size = 4
x2 = torch.randn(6, 2, 4) # Batch size = 6
