
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        tensor = torch.split(x1, [2, 3], dim=1)  # Split tensor along dimension 0
        concatenated_tensor = torch.cat([tensor[i] for i in range(len(tensor))], dim=1)  # Concatenate all split tensors along dimension 0
        return True


# Initializing the model
m = Model()


