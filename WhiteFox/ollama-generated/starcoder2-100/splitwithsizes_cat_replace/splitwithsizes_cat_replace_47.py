
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        splitted = torch.split(x1, 50) # Split the input tensor along axis-0 with size 50 in every call to torch.split
        concatenated = torch.cat([torch.split(splt, 30)[i] for i, splt in enumerate(splitted)])  # Concatenate each split tensor using torch.cat along axis-1 with size 30 on every call to torch.split
        return concatenated, torch.split(x1), torch.split(concatenated)

m = Model()

