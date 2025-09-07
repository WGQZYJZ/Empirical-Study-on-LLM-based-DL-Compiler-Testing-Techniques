
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v7 = torch.cat([x2[:, :, :size], x2[:, :, size:]], dim=1)  # Concatenate the input tensors along dimension 1
 
        return v7


# Initializing the model
m = Model()
 
# Input to the model