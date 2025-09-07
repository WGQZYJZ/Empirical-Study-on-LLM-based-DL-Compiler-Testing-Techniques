
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors)
        v2 = v1[:, 0:9223372036854775807] 
        return v2


# Initializing the model
m = Model()
 
# Input tensors to the model
x1, x2, x3 = torch.randn(1, 3, 64, 64), torch.randn(
    1, 3, 80, 79), torch.randn(
        1, 5, 131, 133)
 
# Calling the forward pass on the model with input tensors as arguments
