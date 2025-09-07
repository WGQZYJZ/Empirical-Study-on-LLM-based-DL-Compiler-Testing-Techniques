
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inputs):
        v0 = torch.cat(inputs) # Concatenate the inputs 
        v1 = v0[:, 0:9223372036854775807]  # Slice along dimension 1
        v2 = v1[:, 0:size]  # Slice along dimension 1
        v3 = torch.cat([v0, v2], dim=1) # Concatenate along dimension 1 
        return v3

# Initializing the model
model  = Model()

# Input tensors to the model
input_tensor_list = [torch.randn(5, 6)] * size
