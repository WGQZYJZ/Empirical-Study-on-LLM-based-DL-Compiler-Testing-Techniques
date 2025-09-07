
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *inputs):
        v0 = torch.cat(inputs[::-1], dim=1) # Concatenate the input tensors along dimension 1 in reverse order
        v1 = v0[:, 9223372036854775807]  # Slice the concatenated tensor along dimension 1 with the last slice size specified by `size`
        return v1

# Initializing the model
m  = Model()
 
# Inputs to the model
size = random.randint(1, 3)
inputs = [torch.randn(random.randint(200), random.randint(100))] * size
__output__  = m(*inputs)