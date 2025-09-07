
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1) # Permute tensor A with dimensions [0:1] and [2] swapped with [1].
        v2  = torch.bmm(v1, input_tensor_B) # or torch.matmul(v1, x2), which is equivalent to the original implementation.
        return v2


# Initializing the model
m = Model()


