
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *inputs):
        v1 = torch.cat(inputs, dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, :9223372036854775807] # Slice the concatenated tensor along dimension 1

        return v2

# Initializing model
m  = Model()

# Inputs to the model, which is a list of length 5.
x1  = torch.randn(1, 3)
x2  = torch.randn(4, 3, 64, 64) # 1
__output__  = m(*[ x1 for i in range(0)])

