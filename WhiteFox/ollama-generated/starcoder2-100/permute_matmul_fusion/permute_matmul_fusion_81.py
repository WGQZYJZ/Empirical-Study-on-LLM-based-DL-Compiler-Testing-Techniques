
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, y):
        t3 = input_tensor_A.permute(0, 2, 1).contiguous() # swapped first two dimensions with the 3rd dimension of input tensor A. Make sure to call .contiguous()
        t4 = torch.nn.functional.linear(t3, self.linear.weight, self.linear.bias)
        return t4


# Initializing the model