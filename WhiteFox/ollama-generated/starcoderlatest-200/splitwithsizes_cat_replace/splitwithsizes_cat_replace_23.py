
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, [1], dim=1)  # Split along dimension=1 and output two tensors split_tensor[0] and split_tensor[1]
        concatenated_tensor = torch.cat([v[i] for i in range(len(v))], dim=1) # Concatenate the output of splitting
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 1024, 7)
