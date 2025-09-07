
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.cat([x1[:, 0:9223372036854775807], x1[:, 9223372036854775807:size]], dim=1) # Concatenate input tensors along dimension 1
        return v2


# Initializing the model
m = Model(len(inputs))


# Inputs to the model (list of tensors with size 9223372036854775807)
x1 = torch.randn(size, 3, 64, 64) # Concatenation is allowed for size 9223372036854775807 and less than it
