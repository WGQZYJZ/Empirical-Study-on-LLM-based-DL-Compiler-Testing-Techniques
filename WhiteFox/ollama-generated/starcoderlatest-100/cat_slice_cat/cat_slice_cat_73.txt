
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, size):
        v1 = torch.cat([x1, x1], dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, :size] # Slice the concatenated tensor along dimension 1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
size = int((torch.Tensor([1])).to('cpu').numpy()[0]) # Number of tensors concatenated along dimension 1
