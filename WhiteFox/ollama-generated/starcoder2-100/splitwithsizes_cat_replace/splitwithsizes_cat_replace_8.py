
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 2048, dim=3) # Split the input tensor into several tensors along dimension 3 (which corresponds to the number of channels in a PyTorch convolutional layer) with sizes 2048 each.
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=3) # Concatenate these split tensors along dimension 3 (which corresponds to the number of channels in a PyTorch convolutional layer).
        return concatenated_tensor

# Initializing the model
m = Model()

