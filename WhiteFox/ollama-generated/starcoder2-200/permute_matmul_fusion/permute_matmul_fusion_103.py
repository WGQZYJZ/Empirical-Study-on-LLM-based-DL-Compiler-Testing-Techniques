
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2): # Assume the input is a dictionary with two tensors (key: 'x', and key: 'y') as elements. 
        x3  = x1.permute(0, 2, 1) # Permute tensor A
        y4  = torch.bmm(x3, y2) # BMM of tensor A and tensor B (tensors have the same dimensions)
        return { 'x': x3, 'y': y4 }

# Initializing the model