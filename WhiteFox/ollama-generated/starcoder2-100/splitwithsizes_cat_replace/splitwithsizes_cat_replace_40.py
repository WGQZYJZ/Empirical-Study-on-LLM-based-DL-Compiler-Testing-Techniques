
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):  # Input tensor 1
        splitted_tensor = torch.split(input1, [8], dim=0) 
        concatenated_tensor = torch.cat([splitted_tensor[i] for i in range(len(splitted_tensor))])  # Concatenate the split tensors along a given dimension using torch.cat
        return concatenated_tensor


# Initializing the model