
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=1)  # Concatenate input tensors along dimension 1
        
        size = (
            v1[:, 0:9223372036854775807].shape[1]
        )  # Calculate the shape of a sliced tensor 
        # along dimension 1 using the original concatenated tensor

        # Slice the original concatenated tensor along dimension 1 by using the
        # calculated size
        
        v2 = v1[:, 0:size]  

        v3 = torch.cat([v1, v2], dim=1)  # Concatenate the sliced and the original tensors 
        return v3


# Initializing the model