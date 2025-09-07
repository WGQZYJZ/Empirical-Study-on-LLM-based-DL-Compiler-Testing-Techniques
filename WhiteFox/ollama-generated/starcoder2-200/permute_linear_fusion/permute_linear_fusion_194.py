
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor by swapping dimensions at index 1 and index 2.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3 ,5, 4) # 4th dimension is 0 for all the tensors in the batch, hence it is not of much concern.
__output__  = m(x1)

