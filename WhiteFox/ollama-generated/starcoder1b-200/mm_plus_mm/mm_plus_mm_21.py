
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(3, 8) # The model has 3 input tensors of dimension 64x64 and 3 output tensors of dimension 8.
        self.mm2 = torch.nn.Linear(8, 8)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + x1  # The last axis of `v1` is a concatenation of two subtensor (a, b), where `a` and `b` are the results of the two matrix multiplications in the input tensor.
        v3 = torch.mm(x1, x1) + x2  # A linear combination of both inputs is computed, which is summed to obtain `v4`.
        return v3


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(3, 64, 64)
input2 = torch.randn(3, 8)
input3 = input1 + input2
